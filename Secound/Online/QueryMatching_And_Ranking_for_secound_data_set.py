import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

inverted_index = np.load(os.path.join(parent_dir, 'Offline\\inverted_index.npy'), allow_pickle=True).item()
cluster_vectors = np.load(os.path.join(parent_dir, 'Offline\\cluster_vectors.npy'), allow_pickle=True).item()
feature_names_path = os.path.join(parent_dir, 'Offline\\feature_names.txt')
feature_names = np.loadtxt(feature_names_path, dtype=str)
term_to_index = {term: index for index, term in enumerate(feature_names)}

def calculate_similarity(query_vector_normalized):
    relevant_documents = []

    query_vector = csr_matrix(query_vector_normalized)

    similarity_scores = []

    for cluster_id, cluster_data in cluster_vectors.items():
        print("Processing Cluster ID:", cluster_id)

        cluster_vector = cluster_data['vector']

        similarity_score = cosine_similarity(query_vector, cluster_vector)[0, 0] 
        similarity_scores.append((cluster_id, similarity_score))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    top_k_clusters = similarity_scores[:2]

    relevant_docs_in_clusters = []
    for cluster_id, similarity_score in top_k_clusters:
        print("Processing Cluster ID s:", cluster_id)
        doc_ids = cluster_vectors[cluster_id]['doc_ids']
        relevant_docs_in_clusters.extend(doc_ids)

    similarity_scores = []
    for doc_id in relevant_docs_in_clusters:
        doc_terms_weights = inverted_index.get(doc_id)
        if doc_terms_weights is not None:
            doc_vector = csr_matrix((1, query_vector.shape[1]), dtype=float) 
            for term, weight in doc_terms_weights:
                term_index = term_to_index.get(term)  
                if term_index is not None:
                    doc_vector[0, term_index] = weight
            similarity_score = cosine_similarity(query_vector, doc_vector)[0, 0]
        if(similarity_score>0.0):
            similarity_scores.append((doc_id, similarity_score))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    relevant_documents = similarity_scores[:10]  

    return relevant_documents

# query_id = 2531329
# processed_text = "Example processed query text"

# query_vector_normalized, feature_names = generate_query_vector(query_id, processed_text)
# relevant_documents = calculate_similarity(query_vector_normalized)

# print("Query ID:", query_id)
# print("Relevant Documents:")
# for doc_id, similarity_score in relevant_documents:
#     print(f"Document ID: {doc_id}, Similarity Score: {similarity_score}")
