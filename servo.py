import board
import neopixel
import RPi.GPIO as GPIO
import time
import gc  

def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False
    start = 4
    end = 12.5
    ratio = (end - start) / 180
    angle_as_percent = angle * ratio
    return start + angle_as_percent

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm_gpio = 23
frequency = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequency)

pin_capteur = 17
GPIO.setup(pin_capteur, GPIO.IN)

pin_servo = 18
GPIO.setup(pin_servo, GPIO.OUT)

pwm_servo = GPIO.PWM(pin_servo, 50)
pwm_servo.start(0)

servo_position = 0

NUM_LEDS = 144
DATA_PIN = board.D21

pixels = neopixel.NeoPixel(DATA_PIN, NUM_LEDS, auto_write=False)

def tourner_servo(angle):
    global servo_position
    duty_cycle = 2.5 + (12.5 - 2.5) * angle / 180.0
    pwm_servo.ChangeDutyCycle(duty_cycle)
    servo_position = angle
    time.sleep(1)

def is_servo_moving():
    if GPIO.input(pin_capteur) == GPIO.LOW:
        if servo_position != 70:
            tourner_servo(70)
        time.sleep(1)
    else:
        if servo_position != 0:
            tourner_servo(0)
        time.sleep(0.1)
    return True

def loop():
    global servo_position

    while True:
        if is_servo_moving():
            for i in range(NUM_LEDS):
                pixels[i] = (255, 0, 0)
            pixels.show()
        else:
            for i in range(NUM_LEDS):
                pixels[i] = (0, 0, 0)
            pixels.show()
        gc.collect() 
        time.sleep(0.1)

try:
    pwm.start(angle_to_percent(0))
    for _ in range(5):
        loop()
        time.sleep(1)

    while True:
        loop()

except KeyboardInterrupt:
    pass

pwm_servo.stop()
GPIO.cleanup()
