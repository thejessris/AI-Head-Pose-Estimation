import cv2
import dlib
import numpy as np

class HeadPoseEstimator:

    def __init__(self):

        self.detector = dlib.get_frontal_face_detector()

        self.predictor = dlib.shape_predictor(
            "models/shape_predictor_68_face_landmarks.dat"
        )

    def process(self, frame):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.detector(gray)

        for face in faces:

            landmarks = self.predictor(gray, face)

            image_points = np.array([
                (landmarks.part(30).x, landmarks.part(30).y),
                (landmarks.part(8).x, landmarks.part(8).y),
                (landmarks.part(36).x, landmarks.part(36).y),
                (landmarks.part(45).x, landmarks.part(45).y),
                (landmarks.part(48).x, landmarks.part(48).y),
                (landmarks.part(54).x, landmarks.part(54).y)
            ], dtype="double")

            model_points = np.array([
                (0.0, 0.0, 0.0),
                (0.0, -330.0, -65.0),
                (-225.0, 170.0, -135.0),
                (225.0, 170.0, -135.0),
                (-150.0, -150.0, -125.0),
                (150.0, -150.0, -125.0)
            ])

            size = frame.shape

            focal_length = size[1]

            center = (
                size[1] / 2,
                size[0] / 2
            )

            camera_matrix = np.array([
                [focal_length, 0, center[0]],
                [0, focal_length, center[1]],
                [0, 0, 1]
            ], dtype="double")

            dist_coeffs = np.zeros((4, 1))

            success, rotation_vector, translation_vector = \
                cv2.solvePnP(
                    model_points,
                    image_points,
                    camera_matrix,
                    dist_coeffs
                )

            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

            pose_matrix = cv2.hconcat(
                (rotation_matrix, translation_vector)
            )

            _, _, _, _, _, _, euler_angles = \
                cv2.decomposeProjectionMatrix(
                    pose_matrix
                )

            pitch = euler_angles[0][0]
            yaw = euler_angles[1][0]
            roll = euler_angles[2][0]

            cv2.putText(
                frame,
                f"Yaw: {int(yaw)}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"Pitch: {int(pitch)}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,0,0),
                2
            )

            cv2.putText(
                frame,
                f"Roll: {int(roll)}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,0,255),
                2
            )

        return frame, {
            "yaw": int(yaw),
            "pitch": int(pitch),
            "roll": int(roll)
        }
