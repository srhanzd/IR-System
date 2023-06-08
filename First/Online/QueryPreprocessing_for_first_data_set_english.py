import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import csv




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

def process_query( query_text):  #query_id,
    cleaned_text = clean_text(query_text)
    tokens = tokenize_text(cleaned_text)
    filtered_tokens = remove_stopwords(tokens)
    stemmed_tokens = stem_tokens(filtered_tokens)
    lemmatized_tokens = lemmatize_tokens(stemmed_tokens)

    processed_text = ' '.join(lemmatized_tokens)
    # return {query_id: processed_text}
    return processed_text



# query_id = "1"
# query_text = "this is  test ???  "
# processed_query = process_query(query_text)#(query_id, query_text)

# # print(processed_query)
