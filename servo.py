import RPi.GPIO as GPIO
import time

pin_capteur = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_capteur, GPIO.IN)

pin_servo = 18
GPIO.setup(pin_servo, GPIO.OUT)

pwm = GPIO.PWM(pin_servo, 50)
pwm.start(0)

servo_position = 0

def tourner_servo(angle):
    global servo_position
    duty_cycle = 2.5 + (12.5 - 2.5) * angle / 180.0
    pwm.ChangeDutyCycle(duty_cycle)
    servo_position = angle
    time.sleep(1)

try:
    while True:
        if GPIO.input(pin_capteur) == GPIO.LOW:
            if servo_position != 70:
                tourner_servo(70)
            time.sleep(1)
        else:
            if servo_position != 0:
                tourner_servo(0)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
