import csv
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
from scipy.sparse import save_npz
from scipy.sparse import load_npz



current_dir = os.path.dirname(os.path.abspath(__file__))




preprocessing_file_path = os.path.join(current_dir,'preprocessing_file.csv')
documents = []
ids = []
with open(preprocessing_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        ids.append(row[0])
        documents.append(row[1])



vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)
normalized_tfidf_matrix = normalize(tfidf_matrix)
ids_array = np.array(ids)

save_npz(os.path.join(current_dir,'normalized_tfidf_matrix.npz'), normalized_tfidf_matrix)
np.save(os.path.join(current_dir,'ids.npy'), ids_array)
np.savetxt(os.path.join(current_dir,'feature_names.txt'), vectorizer.get_feature_names_out(), fmt='%s')

 
normalized_tfidf_matrix = load_npz(os.path.join(current_dir,'normalized_tfidf_matrix.npz'))
ids_array = np.load(os.path.join(current_dir,'ids.npy'))
ids = ids_array.tolist()


feature_names = np.loadtxt(os.path.join(current_dir,'feature_names.txt'), dtype=str)


# id_to_index = {doc_id: index for index, doc_id in enumerate(ids)}

for doc, term, value in zip(normalized_tfidf_matrix.nonzero()[0], normalized_tfidf_matrix.nonzero()[1], normalized_tfidf_matrix.data):
    doc_id = ids[doc]
    # index = id_to_index[doc_id]
    print(f"(doc{doc_id}, {feature_names[term]}) {value}")