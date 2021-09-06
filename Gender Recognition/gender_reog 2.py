import cv2
import Gender_recog as gp
haar=cv2.CascadeClassifier('/home/himanshu/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml')
target=['men','women']
#model=cv2.face.LBPHFaceRecognizer_create()
#model.read('gender_recog.yml')
img=cv2.imread('/home/himanshu/Downloads/Kaagaz_20210117_171900358-1.jpg')
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_rec=haar.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)
for x,y,w,h in face_rec:
    face_roi=grey[y:y+h,x:x+w]
    label, con=gp.model.predict(face_roi)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),thickness=2)
    cv2.putText(img,target[label],(x,y),cv2.FONT_HERSHEY_SIMPLEX,fontScale=3,color=(255,0,0),thickness=2)

cv2.imshow('detect',img)
cv2.waitKey(0)