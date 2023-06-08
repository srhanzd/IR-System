import csv
import re
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize



current_dir = os.path.dirname(os.path.abspath(__file__))


dataset_path = os.path.join(current_dir,'collection.tsv')
preprocessing_output_file_path = os.path.join(current_dir,'preprocessing_file.csv')
 


def clean_text(text):
    cleaned_text = re.sub(r"[^\w\s]", "", text)  
    return cleaned_text.lower()  

def tokenize_text(text):
    tokens = word_tokenize(text) 
    return tokens

def remove_stopwords(tokens):
    stop_words = set(stopwords.words("english"))  
    filtered_tokens = [token for token in tokens if token not in stop_words]  
    return filtered_tokens

def stem_tokens(tokens):
    stemmer = PorterStemmer()  
    stemmed_tokens = [stemmer.stem(token) for token in tokens] 
    return stemmed_tokens

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()  
    tagged_tokens = nltk.pos_tag(tokens)  
    lemmatized_tokens = []
    for token, tag in tagged_tokens:
        pos = get_wordnet_pos(tag)  
        if pos:
            lemmatized_token = lemmatizer.lemmatize(token, pos=pos)  
        else:
            lemmatized_token = lemmatizer.lemmatize(token) 
        lemmatized_tokens.append(lemmatized_token)
    return lemmatized_tokens

def get_wordnet_pos(tag):
    if tag.startswith('N'): 
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith('V'): 
        return nltk.corpus.wordnet.VERB
    elif tag.startswith('R'):  
        return nltk.corpus.wordnet.ADV
    elif tag.startswith('J'):  
        return nltk.corpus.wordnet.ADJ
    else:
        return None


documents = []
ids = []
# i=0
with open(dataset_path, 'r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file, delimiter='\t')

    for row in reader:
        # i=i+1
        # print(i)
        text = row[1] 
        id=row[0] 
       
        cleaned_text = clean_text(text)
        tokens = tokenize_text(cleaned_text)
        filtered_tokens = remove_stopwords(tokens)
        stemmed_tokens = stem_tokens(filtered_tokens)
        lemmatized_tokens = lemmatize_tokens(stemmed_tokens)
        

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



        
         