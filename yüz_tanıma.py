import cv2
import numpy as np

class YuzAlgila():

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)

    def kamera(self):
        while True:
            ret, self.frame = self.cap.read()
            self.Algila()
            self.Cizdir()
            cv2.imshow("Yuz_Algilama", self.frame)
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.cap.release()
                break
    
    def Algila(self):
        self.face_rect = self.face_cascade.detectMultiScale(self.frame, scaleFactor=1.2, minNeighbors=5)

    def Cizdir(self):
        for (x, y, w, h) in self.face_rect:
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (255, 255, 255), 10)


if __name__ == "__main__":
    baslat = YuzAlgila()
    baslat.kamera()
    cv2.destroyAllWindows()
