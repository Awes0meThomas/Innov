import pigpio
import time

pi = pigpio.pi()

pin_capteur = 17
pi.set_mode(pin_capteur, pigpio.INPUT)

pin_servo = 18
pi.set_mode(pin_servo, pigpio.OUTPUT)

servo_position = 0

def tourner_servo(angle):
    global servo_position
    pulse_width = (angle / 180.0 * 1000) + 1000
    pi.set_servo_pulsewidth(pin_servo, pulse_width)
    servo_position = angle
    time.sleep(1)

try:
    while True:
        if pi.read(pin_capteur) == 0:
            if servo_position != 70:
                tourner_servo(70)
            time.sleep(1)
        else:
            if servo_position != 0:
                tourner_servo(0)
        time.sleep(0.1)

except KeyboardInterrupt:
    pi.stop()
