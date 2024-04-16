import cv2
import numpy as np
from gpiozero import AngularServo, DigitalInputDevice
from time import sleep

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

model = cv2.dnn.readNetFromTensorflow('fichier.pb', 'fichier.pbtxt')

def on_activation():
    servo.angle = 180

def on_deactivation():
    servo.angle = 0

try:
    while True:
        image = cv2.imread('test.jpg')

        blob = cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True, crop=False)
        model.setInput(blob)
        output = model.forward()

        rectangle_detected = False
        for detection in output[0, 0, :, :]:
            confidence = detection[2]
            if confidence > 0.5:  
                class_id = int(detection[1])
                if class_id == 0:  
                    x1, y1, x2, y2 = (detection[3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])).astype('int')
                    roi = image[y1:y2, x1:x2]
                    if detect_rectangle(roi):
                        rectangle_detected = True
                        break  

        if rectangle_detected:
            capteur.when_activated = on_activation
            capteur.when_deactivated = on_deactivation
        else:
            capteur.when_activated = None
            capteur.when_deactivated = None

except KeyboardInterrupt:
    pass
