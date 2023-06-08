import csv
import os
from scipy.sparse import load_npz
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

current_dir = os.path.dirname(os.path.abspath(__file__))

queries_preprocessing_file_path = os.path.join(current_dir,'queries_preprocessing_file.csv')
feature_names_path = os.path.join(current_dir,'feature_names.txt')

queries = []
ids = []
with open(queries_preprocessing_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        ids.append(row[0])
        queries.append(row[1])

feature_names = np.loadtxt(feature_names_path, dtype=str)

vectorizer = TfidfVectorizer(vocabulary=feature_names)

vectorizer.fit(queries)

query_vectors = vectorizer.transform(queries)

query_vectors_normalized = normalize(query_vectors)

query_vectors_normalized_dict = {}

for i, query_id in enumerate(ids):
    query_vector_normalized = query_vectors_normalized[i]
    query_vectors_normalized_dict[query_id] = query_vector_normalized

np.save(os.path.join(current_dir,'query_vectors_normalized_dict.npy'), query_vectors_normalized_dict)


query_vectors_normalized_dict = np.load(os.path.join(current_dir,'query_vectors_normalized_dict.npy'), allow_pickle=True).item()

print("Query Vectors Representation:")

for query_id, query_vector in query_vectors_normalized_dict.items():
    print(f"Query ID: {query_id}")
    for term_index, weight in zip(query_vector.indices, query_vector.data):
        term = feature_names[term_index]
        print(f"Term: {term}, Weight: {weight}")
    print("---")