import cv2
import mediapipe as mp
import time


class hand_track():
    def __init__(self, mode=False, max_hands=2, detection_confi=0.5, track_confi=0.5):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mphands = mp.solutions.hands
        self.hand = self.mphands.Hands(mode, max_hands, detection_confi, track_confi)

    def find_hands(self, frame):
        self.results = self.hand.process(frame)
        # print(results.multi_hand_landmarks) #gives the position of the hand
        if self.results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks)
            for handlm in self.results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, handlm, self.mphands.HAND_CONNECTIONS)
        return frame

    def find_position(self, frame, hand_no=0):
        lst_lm = []
        if self.results.multi_hand_landmarks:

            # print(results.multi_hand_landmarks)
            myhand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(myhand.landmark):
                # print(id,lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id,cx,cy)
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                lst_lm.append([id, cx, cy])

        return lst_lm



