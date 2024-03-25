from gpiozero import AngularServo, DigitalInputDevice
import time
import cv2
import numpy as np

pin_cam = 17
pin_servo = 18

capteur = DigitalInputDevice(pin_cam)
servo = AngularServo(pin_servo, min_angle=0, max_angle=180)

net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

def tourner_servo(angle):
    servo.angle = angle
    time.sleep(1)

try:
    while True:
        if capteur.is_active:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            height, width, channels = frame.shape

            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            square_detected = False

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        label = str(classes[class_id])
                        if label == 'square':
                            square_detected = True
                            break

            cap.release()

            if square_detected:
                while not capteur.is_active:
                    pass
                tourner_servo(180)
            else:
                tourner_servo(0)

except KeyboardInterrupt:
    pass
