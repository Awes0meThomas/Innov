import RPi.GPIO as GPIO
import time

def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False
    start = 4
    end = 12.5
    ratio = (end - start) / 180
    angle_as_percent = angle * ratio
    return start + angle_as_percent
GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pwm_gpio = 12
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

infrared_pin = 17

GPIO.setup(infrared_pin, GPIO.IN)


pwm.start(angle_to_percent(0))
time.sleep(1)

try:
    while True:
        if GPIO.input(infrared_pin)==GPIO.LOW:
            pwm.ChangeDutyCycle(angle_to_percent(70))
            time.sleep(1)
            pwm.ChangeDutyCycle(angle_to_percent(0))
            time.sleep(1)
        else:
            time.sleep(1)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
