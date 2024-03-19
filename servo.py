from gpiozero import AngularServo, DigitalInputDevice
from time import sleep
from signal import pause

pin_capteur = 17
capteur = DigitalInputDevice(pin_capteur)

pin_servo = 18
servo = AngularServo(pin_servo, min_angle=0, max_angle=180)

try:
    while True:
        if capteur.is_active:
            servo.angle = 180
        else:
            servo.angle = 0
        sleep(1)

except KeyboardInterrupt:
    pass
