import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

def load_topic_model():
    return pickle.load(open("topic/models/linear_classifier.pkl", 'rb'))

topic_model = load_topic_model()
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('topic/models/label_classes.npy')
topic = label_encoder.inverse_transform(topic_model.predict([input()]))[0]
print(topic)