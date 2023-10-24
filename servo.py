import RPi.GPIO as GPIO
import time


pin_capteur = 17  


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_capteur, GPIO.IN)

try:
    while True:
        if GPIO.input(pin_capteur) == GPIO.HIGH:
            print("Obstacle détecté!")
        else:
            print("Pas d'obstacle détecté.")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
