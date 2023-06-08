import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, 'QueryPreprocessing_for_secound_data_set.py'))
sys.path.append(os.path.join(current_dir, 'QueryRepresention_for_secound_data_set.py'))
sys.path.append(os.path.join(current_dir, 'QueryMatching_And_Ranking_for_secound_data_set.py'))

from QueryPreprocessing_for_secound_data_set import process_query
from QueryRepresention_for_secound_data_set import generate_query_vector
from QueryMatching_And_Ranking_for_secound_data_set import calculate_similarity

def search(query_id, query_text):
    processed_query = process_query(query_text)# (query_id, query_text)
    
    print(processed_query)
    print("---")

    query_id,query_vector_normalized, feature_names = generate_query_vector(query_id, processed_query)
    
    print("Query Vector Representation:")
    print("query_id", query_id)
    for term_index, weight in zip(query_vector_normalized.indices, query_vector_normalized.data):
       term = feature_names[term_index]
       print(f"Term: {term}, Weight: {weight}")
    print("---")

    relevant_documents = calculate_similarity(query_vector_normalized)

    return query_id,relevant_documents

if __name__ == "__main__":
    query_id = 1
    query_text = "Akiolojia (kutoka Kiyunani αρχαίος = \"zamani\" na λόγος = \"neno, usemi\") ni somo linalohusu mabaki ya tamaduni za watu wa nyakati zilizopita. Wanaakiolojia wanatafuta vitu vilivyobaki, kwa mfano kwa kuchimba ardhi na kutafuta mabaki ya majengo, makaburi, silaha, vifaa, vyombo na mifupa ya watu. "
    query_id,relevant_docs = search(query_id, query_text)
    print("query_id: ",query_id)
    print("Relevant Documents:")
    for doc_id, similarity_score in relevant_docs:
        print(f"Document ID: {doc_id}, Similarity Score: {similarity_score}")
