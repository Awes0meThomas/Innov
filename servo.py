from gpiozero import AngularServo, DigitalInputDevice
from signal import pause

pin_capteur = 17
capteur = DigitalInputDevice(pin_capteur)

pin_servo = 18
servo = AngularServo(pin_servo, min_angle=0, max_angle=70)

try:
    while True:
        if capteur.is_active:
            servo.angle = 180
        else:
            servo.angle = 0
        pause()

except KeyboardInterrupt:
    pass
