import time
import RPi.GPIO as GPIO
import board
import neopixel

# Configuration du servo
def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False
    start = 4
    end = 12.5
    ratio = (end - start) / 180
    angle_as_percent = angle * ratio
    return start + angle_as_percent

# Configuration des broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuration du servo
pwm_gpio = 23  # Utilisez le bon numéro de broche BCM
frequency = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequency)

# Configuration du capteur
pin_capteur = 17
GPIO.setup(pin_capteur, GPIO.IN)

# Configuration du servo
pin_servo = 18
GPIO.setup(pin_servo, GPIO.OUT)
pwm_servo = GPIO.PWM(pin_servo, 50)
pwm_servo.start(0)

# Configuration des LED NéoPixel
NUM_LEDS = 144
DATA_PIN = 21  # Utilisez le bon numéro de broche BCM
DELAY_MS = 50

# Assurez-vous que DATA_PIN est correctement configuré
pixels = neopixel.NeoPixel(DATA_PIN, NUM_LEDS, auto_write=False)

# Fonction pour tourner le servo
def tourner_servo(angle):
    duty_cycle = angle_to_percent(angle)
    pwm_servo.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

try:
    pwm_servo.start(angle_to_percent(0))
    
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

# Nettoyage des broches
pwm_servo.stop()
GPIO.cleanup()
