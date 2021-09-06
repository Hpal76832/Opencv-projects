import cv2
import os
import numpy as np

harr=cv2.CascadeClassifier('/home/himanshu/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml')
print(harr)
faces=['man','woman']
labels=[]
features=[]
dir='/home/himanshu/Desktop/opencv_projects/faces/'

for face in faces:
    path=os.path.join(dir+face)
    label=faces.index(face)
    for img in os.listdir(path):
        image=os.path.join(path,img)
        img=cv2.imread(image)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_rec=harr.detectMultiScale(grey,minNeighbors=4,scaleFactor=1.1)
        for x,y,w,h in face_rec:
            face_roi=grey[y:y+h,x:x+w]
            features.append(face_roi)
            labels.append(label)

print(len(features))
#feature=np.array(features,'uint8')
label=np.array(labels)

model=cv2.face.LBPHFaceRecognizer_create()
model.train(features,label)
model.save('gender_recog.yml')