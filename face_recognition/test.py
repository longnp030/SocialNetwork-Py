import cv2

detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_recognition/models/face_model.yml')

img = cv2.imread('post/images/pNone-shige.jpg', cv2.IMREAD_GRAYSCALE)
#print(type(img))

'''faces = detector.detectMultiScale(img, 1.3, 5)
#print(faces)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    id, dist = recognizer.predict(img[y:y+h, x:x+w])
    
    print(dist)
    print(id)'''

cv2.imshow('', img)
cv2.waitKey(0)
cv2.destroyAllWindows()