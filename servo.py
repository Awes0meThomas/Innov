import cv2
import numpy as np
from gpiozero import AngularServo, DigitalInputDevice
from time import sleep
import tensorflow as tf 

model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Initialize the camera capture
camera = cv2.VideoCapture(0)

# Allow the camera to warm up
sleep(2)

pin_capteur = 17
capteur = DigitalInputDevice(pin_capteur)

pin_servo = 18
servo = AngularServo(pin_servo, min_angle=0, max_angle=180)

def detect_rectangle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            return True
    return False

try:
    while True:
        ret, frame = camera.read()  # Capture frame from the camera

        if not ret or frame is None:
            print("Error: Failed to capture frame from the camera.")
            continue  # Skip processing if frame is empty

        # Ensure the frame has valid dimensions
        if frame.shape[0] <= 0 or frame.shape[1] <= 0:
            print("Error: Invalid frame dimensions.")
            continue  # Skip processing if frame dimensions are invalid

        resized = cv2.resize(frame, (224, 224))
        resized = tf.keras.preprocessing.image.img_to_array(resized)
        resized = tf.keras.applications.mobilenet_v2.preprocess_input(resized)

        predictions = model.predict(np.array([resized]))
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)

        rectangle_detected = False
        for _, label, _ in decoded_predictions[0]:
            if label in ["remote", "television", "laptop", "mouse", "keyboard"]:
                rectangle_detected = True
                break  

        if rectangle_detected:
            servo.angle = 180
            capteur.when_activated = lambda: servo.detach()
            capteur.when_deactivated = lambda: servo.attach()
        else:
            servo.angle = 0
            capteur.when_activated = None
            capteur.when_deactivated = None

except KeyboardInterrupt:
    pass

# Release the camera
camera.release()
