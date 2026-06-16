import os
import urllib.request
import bz2

MODEL_URL = (
    "https://dlib.net/files/"
    "shape_predictor_68_face_landmarks.dat.bz2"
)

os.makedirs("models", exist_ok=True)

print("Downloading model...")

urllib.request.urlretrieve(
    MODEL_URL,
    "models/model.bz2"
)

print("Extracting...")

with bz2.BZ2File(
    "models/model.bz2"
) as fr:
    data = fr.read()

with open(
    "models/shape_predictor_68_face_landmarks.dat",
    "wb"
) as fw:
    fw.write(data)

print("Done!")
