import cv2

haar_cas=cv2.CascadeClassifier('/home/himanshu/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
people=['ben affleck','henry cavil','tom cruise']

face_recog=cv2.face.LBPHFaceRecognizer_create()
face_recog.read('train_model.yml')

img=cv2.imread('/home/himanshu/Desktop/images/ben affleck/2.jpeg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_rec=haar_cas.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)

for x,y,w,h in face_rec:
    face_roi=grey[y:y+h,x:x+w]
    labels, confidence=face_recog.predict(face_roi)
    print(people[labels],confidence)
    cv2.putText(img,people[labels],(20,20),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('detect',img)
cv2.waitKey(0)