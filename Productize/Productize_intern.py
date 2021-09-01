import cv2
import os
import numpy as np
'''#arr=np.ones((300,300),dtype=float)
#or
arr=np.full((300,300),255,dtype=float)
cv2.rectangle(arr,(100,100),(200,200),color=(0,255,255),thickness=4)
cv2.circle(arr,(100,100),radius=50,color=(0,255,255),thickness=4)
cv2.line(arr,(200,100),(100,200),color=(0,255,255),thickness=4)

cv2.imshow('win',arr)
cv2.imwrite('result1.png',arr)
cv2.waitKey(0)'''

'''img=cv2.imread('/home/himanshu/Desktop/Productize CV intern/input1/2.png')
img=cv2.resize(img,(500,500))
#i=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cv2.imshow('win',img)
cv2.imwrite('result3.png',img)
cv2.waitKey(0)'''


#wireframe 1

'''img=np.full((480,480,3),255,dtype=float)
ble=img.copy()

alpha=0.1

cv2.rectangle(img,(0,0),(240,100),color=(0,255,0),thickness=-1)
cv2.rectangle(img,(240,240),(480,340),color=(0,255,0),thickness=-1)
cv2.rectangle(img,(240,240),(340,480),color=(0,0,220),thickness=-1)
cv2.rectangle(img,(0,240),(240,480),color=(2,0,0),thickness=-1)
cv2.rectangle(img,(240,240),(340,340),color=(250,255,0),thickness=-1)

out = cv2.addWeighted(img, alpha, ble,1-alpha, 0,ble)

cv2.putText(out,'text',(30,70),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'text',(340,300),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'photo',(250,400),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)
cv2.putText(out,'object',(50,400),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)

#cv2.imshow('win',img)
#acv2.imshow('wind',blk)
cv2.imshow('blend',out)
cv2.imwrite('result4.png',out)
cv2.waitKey(0)
cv2.destroyAllWindows()'''





#wireframe 2

'''img=np.full((480,960,3),255,dtype=float)
ble=img.copy()

alpha=0.1

cv2.rectangle(img,(0,0),(240,100),color=(0,255,0),thickness=-1)
cv2.rectangle(img,(480,240),(720,340),color=(0,255,0),thickness=-1)
cv2.rectangle(img,(480,240),(580,480),color=(0,0,220),thickness=-1)
cv2.rectangle(img,(0,240),(240,480),color=(2,0,0),thickness=-1)
cv2.rectangle(img,(480,240),(580,340),color=(250,255,0),thickness=-1)

out = cv2.addWeighted(img, alpha, ble,1-alpha, 0,ble)

cv2.putText(out,'text',(30,70),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'text',(590,300),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'photo',(490,390),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)
cv2.putText(out,'object',(50,400),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)

#acv2.imshow('wind',blk)
cv2.imshow('blend',out)
cv2.imwrite('result5.png',out)
cv2.imshow('win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

 #wireframe 3


'''img=np.full((960,480,3),255,dtype=float)
ble=img.copy()

alpha=0.1

#cv2.rectangle(img,(0,100),(300,400),color=(0,15,255),thickness=-1)#big last

cv2.rectangle(img,(0,0),(240,100),color=(0,255,0),thickness=-1)
cv2.rectangle(img,(0,240),(240,480),color=(255,0,0),thickness=-1)#blue 2


cv2.rectangle(img,(200,200),(220,400),color=(0,0,255),thickness=-1)# not done

cv2.rectangle(img,(480,0),(780,100),color=(255,0,0),thickness=-1)
cv2.rectangle(img,(0,0),(100,100),color=(255,0,0),thickness=-1)

cv2.rectangle(img,(480,240),(720,480),color=(0,255,0),thickness=-1)# big
cv2.rectangle(img,(480,240),(720,340),color=(255,0,0),thickness=-1)#blue
cv2.rectangle(img,(480,240),(580,480),color=(0,0,255),thickness=-1)#red
cv2.rectangle(img,(480,240),(580,340),color=(0,255,0),thickness=-1)#green
#cv2.rectangle(img,(0,240),(240,480),color=(0,50,100),thickness=20)#big yellow

cv2.rectangle(img,(200,200),(400,400),color=(150,200,0),thickness=-1)#sky blue


cv2.rectangle(img,(300,300),(360,360),color=(255,0,0),thickness=-1)


cv2.rectangle(img,(300,300),(350,360),color=(0,0,255),thickness=-1)


cv2.rectangle(img,(0,100),(300,400),color=(0,0,0),thickness=-1)#yellow

cv2.rectangle(img,(0,100),(40,400),color=(0,0,255),thickness=-1)#red long
cv2.rectangle(img,(0,240),(40,400),color=(0,255,0),thickness=-1)


cv2.rectangle(img,(222,200),(300,400),color=(0,255,0),thickness=-1)

cv2.rectangle(img,(200,200),(220,400),color=(0,0,255),thickness=-1)
cv2.rectangle(img,(200,240),(220,400),color=(0,255,0),thickness=-1)


cv2.rectangle(img,(100,100),(400,110),color=(150,200,0),thickness=-1)


cv2.rectangle(img,(300,100),(400,110),color=(0,255,0),thickness=-1)

cv2.rectangle(img,(100,100),(110,110),color=(0,0,255),thickness=-1)

cv2.rectangle(img,(40,240),(200,400),color=(0,0,255),thickness=-1)#blue 2

cv2.rectangle(img,(220,240),(240,400),color=(255,0,0),thickness=-1)




cv2.rectangle(img,(480,0),(580,100),color=(0,255,0),thickness=-1)


out = cv2.addWeighted(img, alpha, ble,1-alpha, 0,ble)

cv2.putText(out,'text',(110,70),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'text',(590,300),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(0,0,0),thickness=4)
cv2.putText(out,'text',(490,390),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)
cv2.putText(out,'text',(50,440),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)
cv2.putText(out,'photo',(200,300),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.2,color=(0,0,0),thickness=2)


cv2.putText(out,'photo',(340,108),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.2,color=(0,0,0),thickness=2)
cv2.putText(out,'photo',(2,190),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,0),thickness=2)
cv2.putText(out,'object',(600,50),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=4)
cv2.putText(out,'object',(300,340),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5,color=(0,0,0),thickness=2)
cv2.putText(out,'text',(20,70),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)

cv2.putText(out,'text',(500,300),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)
cv2.putText(out,'text',(630,420),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)
cv2.putText(out,'text',(60,320),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)
cv2.putText(out,'photo',(300,240),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)
cv2.putText(out,'photo',(100,109),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.1,color=(0,0,0),thickness=2)

cv2.putText(out,'object',(480,60),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,0),thickness=2)

cv2.putText(out,'object',(350,320),cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.1,color=(0,0,0),thickness=2)

cv2.putText(out,'photo',(70,180),cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,255,255),thickness=2)


#acv2.imshow('wind',blk)
cv2.imshow('blend',out)
cv2.imwrite('result6.png',out)
cv2.imshow('win',img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



#Bonus task

def nothing(x):
    pass

cv2.namedWindow('trackbar')

cv2.createTrackbar('l_h','trackbar',0,255,nothing)

cv2.createTrackbar('l_s','trackbar',0,255,nothing)

cv2.createTrackbar('l_v','trackbar',0,255,nothing)

cv2.createTrackbar('u_h','trackbar',255,255,nothing)

cv2.createTrackbar('u_s','trackbar',255,255,nothing)

cv2.createTrackbar('u_v','trackbar',255,255,nothing)

while True:
    img1 = cv2.imread('/home/himanshu/Desktop/Productize CV intern/input2/3.jpg')
    img = cv2.resize(img1, (500, 500))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos('l_h','trackbar')

    ls=cv2.getTrackbarPos('l_s','trackbar')

    lv=cv2.getTrackbarPos('l_v','trackbar')

    uh=cv2.getTrackbarPos('u_h','trackbar')

    us=cv2.getTrackbarPos('u_s','trackbar')

    uv=cv2.getTrackbarPos('u_v','trackbar')

    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,lb,ub)
    canny=cv2.Canny(mask,100,200)
    res=cv2.bitwise_and(img,img,mask=mask)


    contours, hiera=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #print('total cigrates',len(contours))

    for contour in contours:
        area=cv2.contourArea(contour)

        if area<10:
            cv2.drawContours(img,contour,-1,color=(0,255,0),thickness=2)




    cv2.imshow('win',img)
    cv2.imshow('res',res)
    cv2.imshow('mask',mask)
    cv2.imshow('canny',canny)
    key=cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()







