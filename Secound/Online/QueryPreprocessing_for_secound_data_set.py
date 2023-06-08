import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import csv
from nltk.corpus import wordnet





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

def process_query( query_text):  #query_id,
    cleaned_text = clean_text(query_text)
    tokens = tokenize_text(cleaned_text)
    filtered_tokens = remove_stopwords(tokens)
    lemmatized_tokens = lemmatize_tokens(filtered_tokens)

    processed_text = ' '.join(lemmatized_tokens)
    # return {query_id: processed_text}
    return processed_text



# query_id = "1"
# query_text = "this is  test ???  "
# processed_query = process_query(query_text)#(query_id, query_text)

# # print(processed_query)
