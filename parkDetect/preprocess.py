import numpy as np
import cv2

def process_image(image):
    test_data = []
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (256, 256))

    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]


    # loaded_model = joblib.load("trained_models/rfc.pkl")
    # result = loaded_model.predict(testX)

    return image