import cv2
import os
import numpy as np
haar_cas=cv2.CascadeClassifier('/home/himanshu/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
print('haar_cas')
people=['ben affleck','henry cavil','tom cruise']
labels=[]
features=[]
DIR=r"/home/himanshu/Desktop/images"
for person in people:
    path = os.path.join(DIR,person)
    label=people.index(person)
    for img in os.listdir(path):
        img=os.path.join(path,img)
        img=cv2.imread(img)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_rec=haar_cas.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=4)
        for x,y,w,h in face_rec:
            face_roi=grey[y:y+h,x:x+w]
            features.append(face_roi)
            labels.append(label)


features=np.array(features)
labels=np.array(labels)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)
print(labels)
face_recognizer.save('train_model.yml')