import re
import ast
from underthesea import word_tokenize

def remove_html(text):
    return re.sub(r'<[^>]*>', '', text)

def remove_punct(text):
    return re.sub(r'[^\s\wáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệóòỏõọôốồổỗộơớờởỡợíìỉĩịúùủũụưứừửữựýỳỷỹỵđ_]', ' ', text)

def remove_spaces(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_stopwords(text):
    stopwords = []
    with open('topic/data/stopwords.txt', 'r', encoding='utf-8') as f:
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
    '''data = {}
    with open(file, 'r', encoding='utf-8') as f:
        raw_data = ast.literal_eval(f.read())
        for topic, texts in raw_data.items():
            topic = lower(topic).strip().replace(' ', '_')

            standardized_texts = []
            for text in texts:
                text = standardize(text)
                standardized_texts.append(text)
            
            data[topic] = standardized_texts
    
    with open('topic/data/standardized_data.txt', 'w+', encoding='utf-8') as f:
        print(data, file=f)'''

    '''data = []
    with open(file, 'r', encoding='utf-8') as f:
        no_topic_data = ast.literal_eval(f.read())
        for text in no_topic_data:
            data.append(standardize(text))
    with open('topic/data/standardized_for_test.txt', 'w+', encoding='utf-8') as f:
        print(data, file=f)'''

make_standard_data('topic/data/standardized_data.txt')
