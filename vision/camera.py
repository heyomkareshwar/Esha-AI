import cv2

class Camera:
    def __init__(self):
        self.cap=None
    def start(self):
        if self.cap is None:
            self.cap=cv2.VideoCapture(0)
        return self.cap.isOpened()
    def read(self):
        if self.cap is None:
            return False,None
        return self.cap.read()
    def stop(self):
        if self.cap:
            self.cap.release()
            self.cap=None
