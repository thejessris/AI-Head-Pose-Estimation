import dlib
import cv2


class FaceDetector:

    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()

    def detect(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.detector(gray)

        return faces
