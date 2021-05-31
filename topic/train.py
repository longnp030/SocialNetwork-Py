from post.views import standardize
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import numpy as np
import pickle
import time
import ast

text = []
label = []

with open('topic/data/standardized_data.txt', 'r', encoding='utf-8') as f:
    data = ast.literal_eval(f.read())
    for topic, texts in data.items():
        for txt in texts:
            label.append(topic)
            text.append(txt)

X_train, X_test, y_train, y_test = train_test_split(text, label, test_size=0.2, random_state=42)

'''with open('topic/data/train.txt', 'w+', encoding='utf-8') as f:
    for x, y in zip(X_train, y_train):
        f.write('{} {}\n'.format(y, x))
with open('topic/data/test.txt', 'w+', encoding='utf-8') as f:
    for x, y in zip(X_test, y_test):
        f.write('{} {}\n'.format(y, x))'''

label_encoder = LabelEncoder()
label_encoder.fit(y_train)
#np.save('topic/models/label_classes.npy', label_encoder.classes_)
print(list(label_encoder.classes_), '\n')
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

### Train
'''start_time = time.time()

print('Start training ...')
text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                             max_df=0.8,
                                             max_features=None)), 
                     ('tfidf', TfidfTransformer()),
                     ('clf', LogisticRegression(solver='lbfgs', 
                                                multi_class='auto',
                                                max_iter=10000))
                    ])
text_clf = text_clf.fit(X_train, y_train)
 
train_time = time.time() - start_time
print('Done training Linear Classifier in', train_time, 'seconds.')
 
# Save model
pickle.dump(text_clf, open("topic/models/linear_classifier.pkl", 'wb'))'''

### Evaluate
model = pickle.load(open("topic/models/linear_classifier.pkl", 'rb'))
'''y_pred = model.predict(X_test)
print('Linear Classifier, Accuracy =', np.mean(y_pred == y_test))
print(classification_report(y_test, y_pred, target_names=list(label_encoder.classes_)[:22]))'''

y_pred = model.predict([standardize(input("Văn bản: "))])
print("Chủ đề dự đoán: ", label_encoder.inverse_transform(y_pred))
