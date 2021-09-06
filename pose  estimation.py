import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)
drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose
pose=mp_pose.Pose()

while True:
    _, frame=cap.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=pose.process(img)
    #print(result.pose_landmarks)
    if result.pose_landmarks:
        drawing.draw_landmarks(img,result.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        for id,lm in enumerate(result.pose_landmarks.landmark):
            #print(id,lm)
            h, w, c=img.shape
            cx, cy=int(lm.x * w), int(lm.y * h)
            print(id,cx,cy)


    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

