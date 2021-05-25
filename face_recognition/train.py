import os
import cv2
import numpy as np
import image
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

print(os.path.isdir('face_recognition/data'))
print(os.listdir('face_recognition/data'))
def getImgAndLabels(path):
    imgPaths = [os.path.join(path, f) for f in os.listdir(path)]

    faceSamples = []
    IDs = []

    for imgPath in imgPaths:
        pilImg = Image.open(imgPath).convert('L')
        imgNp = np.array(pilImg, 'uint8')
        ID = int(os.path.split(imgPath)[-1].split('.')[0])

        faces = detector.detectMultiScale(imgNp)

        for (x, y, w, h) in faces:
            faceSamples.append(imgNp[y:y+h, x:x+w])
            IDs.append(ID)
    
    return faceSamples, IDs

faceSamples, IDs = getImgAndLabels('face_recognition/data/train')

recognizer.train(faceSamples, np.array(IDs))

recognizer.save('face_recognition/models/face_model.yml')
print('done')