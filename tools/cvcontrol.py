import cv2
import mediapipe as mp
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

class CvControl:
    def __init__(self,drone):
        self.handControlState = True
        self.IMG = []
        self.drone = drone
        # self.widget = widget
        # self.display_width = widget.frameGeometry().width()
        # self.display_height = widget.frameGeometry().height()

        self.cap = cv2.VideoCapture(0)


    def detectControl(self):
        posMain = []

        with mp_hands.Hands(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as mains:
            if self.cap.isOpened() and self.handControlState:
                success, image = self.cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    return

                # Flip the image horizontally for a later selfie-view display, and convert
                # the BGR image to RGB.
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                image.flags.writeable = False
                results = mains.process(image)

                # Draw the hand annotations on the image.
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                self.display_width = image.shape[1]
                self.display_height = image.shape[0]

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        Y = hand_landmarks.landmark[0].y * self.display_height
                        X = hand_landmarks.landmark[0].x * self.display_width
                        cv2.circle(image,(int(X),int(Y)),5,color=(255, 0, 0), thickness=-1)
                        posMain.append((int(X),int(Y)))


                        # mp_drawing.draw_landmarks(
                        #     image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                self.IMG = image.copy()
        if len(posMain)>1 :
            cv2.line(self.IMG,posMain[0],posMain[1],(255, 0, 0),thickness=5)
            coteOppose = posMain[0][1] - posMain[1][1]
            coteAdjacent = posMain[1][0] - posMain[0][0]
            tangente = coteOppose/coteAdjacent
            teta = math.atan(tangente) * 180.0 / math.pi

            diff = self.drone.alpha - self.drone.teta

            self.drone.teta = teta
            self.drone.alpha = diff + teta
            self.drone.actor.setHpr(teta, 0, 0)
            print(teta)

        cv2.imshow('Opencv drone control', self.IMG)
        #self.displayImage()

    def runControl(self):
        # For webcam input:
        cap = cv2.VideoCapture(0)
        with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
          while cap.isOpened() and self.handControlState:
            success, image = cap.read()
            if not success:
              print("Ignoring empty camera frame.")
              # If loading a video, use 'break' instead of 'continue'.
              continue

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            data = [];
            if results.multi_hand_landmarks:

              for hand_landmarks in results.multi_hand_landmarks:
                for data_point in hand_landmarks.landmark:
                  data.append({
                    'X': data_point.x,
                    'Y': data_point.y,
                    'Z': data_point.z
                  })

                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # cv2.imshow('MediaPipe Hands', image)
            self.IMG = image
            self.displayImage()
            if results.multi_handedness:
              for hand_landmarks in results.multi_handedness:
                print(hand_landmarks)
            if cv2.waitKey(5) & 0xFF == 27:
              break
        cap.release()

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def displayImage(self):
        self.widget.setPixmap(self.convert_cv_qt(self.IMG))

