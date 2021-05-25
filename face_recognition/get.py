import cv2

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

sampleNum=0
id = 3
while(True):
    ret, img = cam.read()
    print(img)
    print(type(img))
    # Lật ảnh cho đỡ bị ngược
    img = cv2.flip(img,1)

    # Kẻ khung giữa màn hình để người dùng đưa mặt vào khu vực này
    centerH = img.shape[0] // 2;
    centerW = img.shape[1] // 2;
    sizeboxW = 300;
    sizeboxH = 400;
    cv2.rectangle(img, (centerW - sizeboxW // 2, centerH - sizeboxH // 2),
                  (centerW + sizeboxW // 2, centerH + sizeboxH // 2), (255, 255, 255), 5)

    # Đưa ảnh về ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Nhận diện khuôn mặt
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # Vẽ hình chữ nhật quanh mặt nhận được
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        sampleNum = sampleNum + 1
        # Ghi dữ liệu khuôn mặt vào thư mục data
        cv2.imwrite("face_recognition/data/train/" + str(id) + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])

    cv2.imshow('frame', img)
    
    if sampleNum >= 500:
        break

cam.release()
cv2.destroyAllWindows()