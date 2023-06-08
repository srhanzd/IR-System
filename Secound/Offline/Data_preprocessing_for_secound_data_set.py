import csv
import re
import nltk
import json
import os 
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

current_dir = os.path.dirname(os.path.abspath(__file__))



dataset_path = os.path.join(current_dir, 'docs.jsonl')
preprocessing_output_file_path = os.path.join(current_dir, 'preprocessing_file.csv')


def clean_text(text):
    cleaned_text = re.sub(r"[^\w\s]", "", text)
    return cleaned_text.lower()

def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens


custom_stopwords = [
    'akasema', 'alikuwa', 'alisema', 'baada', 'basi', 'bila', 'cha', 'chake', 'changu', 'chao',
    'cha', 'hayo', 'hii', 'hivyo', 'huku', 'huo', 'ili', 'ilikuwa', 'juu', 'kama', 'karibu',
    'katika', 'kila', 'kima', 'kisha', 'kubwa', 'kutoka', 'kuwa', 'kwamba', 'kwangu', 'kwa',
    'kwake', 'kwako', 'kwanza', 'kwetu', 'kwenye', 'la', 'lakini', 'mara', 'mdogo', 'mimi',
    'moja', 'muda', 'mwenye', 'na', 'ndani', 'ng', 'ni', 'nini', 'nonkungu', 'pamoja', 'pia',
    'sana', 'sasa', 'sauti', 'tafadhali', 'tena', 'tu', 'vile', 'wa', 'wakati', 'wake',
    'wale', 'walikuwa', 'wao', 'watu', 'wengine', 'wote', 'ya', 'yake', 'yako', 'yangu',
    'yao', 'yetu', 'yeye', 'yule', 'za', 'zaidi', 'zake'
]
def remove_stopwords(tokens):
    filtered_tokens = [token for token in tokens if token not in custom_stopwords]
    return filtered_tokens


def lemmatize_tokens(tokens):
    lemmatizer = nltk.WordNetLemmatizer()
    lemmatized_tokens = []
    for token in tokens:
        pos = get_wordnet_pos(token)
        if pos:
            lemmatized_token = lemmatizer.lemmatize(token, pos=pos)
        else:
            lemmatized_token = lemmatizer.lemmatize(token)
        lemmatized_tokens.append(lemmatized_token)
    return lemmatized_tokens

def get_wordnet_pos(token):
    tag = nltk.pos_tag([token])[0][1][0].upper()
    if tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('R'):
        return wordnet.ADV
    elif tag.startswith('J'):
        return wordnet.ADJ
    else:
        return None

    
    
documents = []
ids = []
i = 0
with open(dataset_path, 'r', encoding='utf-8') as file:
    for line in file:
        row = json.loads(line)

        # i += 1
        # print(i)
        text = row['contents'] 
        id = row['id'] 
       
        cleaned_text = clean_text(text)
        tokens = tokenize_text(cleaned_text)
        filtered_tokens = remove_stopwords(tokens)
        lemmatized_tokens = lemmatize_tokens(filtered_tokens)
        
        processed_text = ' '.join(lemmatized_tokens)
        documents.append(processed_text)
        ids.append(id)
        print("Original Text: ", text)
        print("Processed Tokens: ", lemmatized_tokens)
        print("---")
       
with open(preprocessing_output_file_path, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.writer(output_file)
    for id, processed_text in zip(ids, documents):
        writer.writerow([id, processed_text])
