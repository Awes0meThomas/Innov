import neopixel
import board
import time
import RPi.GPIO as GPIO

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

pwm = GPIO.PWM(pin_servo, 50)
pwm.start(0)

servo_position = 0

NUM_LEDS = 144
DATA_PIN = board.D21
DELAY_MS = 50
BUTTON_PIN = 2

pixels = neopixel.NeoPixel(board.D21, NUM_LEDS, auto_write=False)

def is_servo_moving():
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
        pass

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

pwm.stop()
GPIO.cleanup()
