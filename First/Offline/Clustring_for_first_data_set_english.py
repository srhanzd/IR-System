import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from scipy.sparse import csr_matrix

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'inverted_index.npy')


inverted_index = np.load(file_path, allow_pickle=True).item()

documents = [' '.join([term for term, _ in postings]) for postings in inverted_index.values()]

vectorizer = TfidfVectorizer()
term_vectors = vectorizer.fit_transform(documents)

num_clusters =100 #40  20
clustering = KMeans(n_clusters=num_clusters)
cluster_labels = clustering.fit_predict(term_vectors)

cluster_vectors = {}
term_to_index = {term: index for index, term in enumerate(vectorizer.get_feature_names_out())}

for doc_id, label in zip(inverted_index.keys(), cluster_labels):
    doc_terms_weights = inverted_index.get(doc_id)
    if doc_terms_weights is not None:
        doc_vector = csr_matrix((1, term_vectors.shape[1]), dtype=float) 
        for term, weight in doc_terms_weights:
            term_index = term_to_index.get(term)  
            if term_index is not None:
                doc_vector[0, term_index] = weight

        if label not in cluster_vectors:
            cluster_vectors[label] = {
                'vector': doc_vector,
                'doc_ids': [doc_id]
            }
        else:
            cluster_vectors[label]['vector'] += doc_vector
            cluster_vectors[label]['doc_ids'].append(doc_id)

for label, cluster_data in cluster_vectors.items():
    doc_ids = cluster_data['doc_ids']
    cluster_data['vector'] /= len(doc_ids)
    # print(doc_ids)
    

cluster_vectors_file = os.path.join(current_dir, 'cluster_vectors.npy')
np.save(cluster_vectors_file, cluster_vectors)

print("Cluster vectors saved to cluster_vectors.npy.")