import cv2


class Camera:

    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def read(self):

        success, frame = self.cap.read()

        return success, frame

    def release(self):

        self.cap.release()
