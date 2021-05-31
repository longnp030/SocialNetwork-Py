from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from underthesea import word_tokenize
import pandas as pd
import pickle
import re

def get_vectorizer(option, name='tf_idf'):
    if option == 'generate':
        if name == 'tf_idf':
            vectorizer = TfidfVectorizer(
                tokenizer=tokenize,
                ngram_range=(1, 4),
                min_df=5,
                max_df=0.8,
                max_features=5000,
                sublinear_tf=True
            )
        else:
            vectorizer = CountVectorizer(
                tokenizer=tokenize,
                ngram_range=(1, 4),
                min_df=5,
                max_df=0.8,
                max_features=5000,
                sublinear_tf=True
            )
    elif option == 'load':
        if name == 'tf_idf':
            vectorizer = TfidfVectorizer(
                vocabulary=pickle.load(open('sentiment/models/vocabulary.pkl', 'rb')),
                ngram_range=(1,3),
                min_df=5,
                max_df=0.8,
                max_features=15000,
                sublinear_tf=True
            )
        else:
            vectorizer = CountVectorizer(
                vocabulary=pickle.load(open('sentiment/models/vocabulary.pkl', 'rb')),
                ngram_range=(1,3),
                min_df=5,
                max_df=0.8,
                max_features=15000,
                sublinear_tf=True
            )
    return vectorizer

def remove_punct(text):
    return re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]', ' ', text)

def remove_html(text):
    return re.sub(r'<[^>]*>', '', text)

def remove_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_stopwords(text):
    stopwords = []
    with open('sentiment/data/stopwords.txt', 'r', encoding='utf-8') as f:
        for stopword in f.readlines():
            stopwords.append(stopword.strip())

    return ' '.join([word for word in text.split() if word not in stopwords])

def lower(text):
    return text.lower()

def standardize(text):
    text = remove_html(text)
    text = word_tokenize(text, format='text')
    text = lower(text)
    text = remove_punct(text)
    text = remove_spaces(text)
    text = remove_stopwords(text)
    return text

def make_standard_data(file):
    data = {}
    with open(file, 'r', encoding='utf-8') as f:
        raw_data = pd.read_csv(f)
        for index, row in raw_data.iterrows():
            rate = row['rate']
            text = standardize(row['comment'])
            data[text] = rate
    
    with open('sentiment/data/standardized_data.txt', 'w+', encoding='utf-8') as f:
        print(data, file=f)

make_standard_data('sentiment/data/data.csv')
