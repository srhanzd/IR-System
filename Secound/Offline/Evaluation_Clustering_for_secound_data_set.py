import numpy as np
import os 
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
current_dir = os.path.dirname(os.path.abspath(__file__))



inverted_index = np.load(os.path.join(current_dir, 'inverted_index.npy'), allow_pickle=True).item()
query_vectors_normalized_dict = np.load(os.path.join(current_dir, 'query_vectors_normalized_dict.npy'), allow_pickle=True).item()
feature_names_path = os.path.join(current_dir, 'feature_names.txt')
feature_names = np.loadtxt(feature_names_path, dtype=str)
cluster_vectors_file = os.path.join(current_dir, 'cluster_vectors.npy')
qrels_file_path = os.path.join(current_dir, 'file.qrels')
output_file_path = os.path.join(current_dir, 'clustering_evaluation_results.txt')

cluster_vectors = np.load(cluster_vectors_file, allow_pickle=True).item()

term_to_index = {term: index for index, term in enumerate(feature_names)}

relevant_documents = {}

with open(qrels_file_path, 'r') as f:
    for line in f:
        query_id, doc_id, relevance, iteration = line.strip().split("\t")

        if query_id not in relevant_documents:
            relevant_documents[query_id] = []

        relevant_documents[query_id].append((doc_id, relevance))

precision_10 = 0
total_precision = 0
total_precision_10=0
total_recall = 0
total_average_precision = 0
total_reciprocal_rank = 0
total_queries = len(relevant_documents)

output_lines = [] 

for query_id, query_vector in query_vectors_normalized_dict.items():
    if query_id in relevant_documents:
        output_lines.append(f"Query ID: {query_id}")

        query_vector = csr_matrix(query_vector)  

        similarity_scores = []

        for cluster_id, cluster_data in cluster_vectors.items():
            cluster_vector = cluster_data['vector']

            similarity_score = cosine_similarity(query_vector, cluster_vector)[0, 0]
            similarity_scores.append((cluster_id, similarity_score))

        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        top_k_clusters = similarity_scores[:2]  

        retrieved_docs_in_clusters = []
        for cluster_id, similarity_score in top_k_clusters:
            doc_ids = cluster_vectors[cluster_id]['doc_ids']
            retrieved_docs_in_clusters.extend(doc_ids)

        similarity_scores = []
        for doc_id in retrieved_docs_in_clusters:
            if doc_id in [d for d, _ in relevant_documents.get(query_id, [])]:
                doc_terms_weights = inverted_index.get(doc_id)
                if doc_terms_weights is not None:
                    doc_vector = csr_matrix((1, query_vector.shape[1]), dtype=float)
                    relevant_docs = [doc_id for doc_id, _ in relevant_documents[query_id]]
                    for term, weight in doc_terms_weights:
                        term_index = term_to_index.get(term)
                        if term_index is not None:
                            doc_vector[0, term_index] = weight
                    similarity_score = cosine_similarity(query_vector, doc_vector)[0, 0]
                    similarity_scores.append((doc_id, similarity_score))

        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        precision = 0
        precision_10=0
        recall = 0

        if len(similarity_scores) > 0:
            precision_10 = sum([1 for doc_id, _ in similarity_scores[:10] if doc_id in relevant_docs]) / 10
            precision = sum([1 for doc_id, _ in similarity_scores if doc_id in relevant_docs]) / len(similarity_scores)
            recall = sum([1 for doc_id, _ in similarity_scores if doc_id in relevant_docs]) / len(relevant_docs)

        total_precision += precision
        total_precision_10 += precision_10
        total_recall += recall

        average_precision = 0
        num_relevant_docs = 0

        for i, (doc_id, score) in enumerate(similarity_scores):
            if doc_id in relevant_docs:
                num_relevant_docs += 1
                precision_at_i = num_relevant_docs / (i + 1)
                average_precision += precision_at_i

        if num_relevant_docs > 0:
            average_precision /= num_relevant_docs

        total_average_precision += average_precision

        reciprocal_rank = 0
        for i, (doc_id, score) in enumerate(similarity_scores):
            if doc_id in relevant_docs:
                reciprocal_rank = 1 / (i + 1)
                break

        total_reciprocal_rank += reciprocal_rank
        


        output_lines.append("Precision@10: {:.2f}".format(precision_10))
        output_lines.append("Precision: {:.2f}".format(precision))
        output_lines.append("Recall: {:.2f}".format(recall))
        output_lines.append("Average Precision: {:.2f}".format(average_precision))
        output_lines.append("Reciprocal Rank: {:.2f}".format(reciprocal_rank))
        output_lines.append("---")

mean_precision_10 = total_precision_10 / total_queries
mean_precision = total_precision / total_queries
mean_recall = total_recall / total_queries
mean_average_precision = total_average_precision / total_queries
mean_reciprocal_rank = total_reciprocal_rank / total_queries

output_lines.append("Mean Precision@10: {:.2%}".format(mean_precision_10))
output_lines.append("Mean Precision: {:.2%}".format(mean_precision))
output_lines.append("Mean Recall: {:.2%}".format(mean_recall))
output_lines.append("Mean Average Precision: {:.2%}".format(mean_average_precision))
output_lines.append("Mean Reciprocal Rank: {:.2%}".format(mean_reciprocal_rank))

with open(output_file_path, 'w') as f:
    f.write("\n".join(output_lines))

print("Evaluation results saved to:", output_file_path)
