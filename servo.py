import RPi.GPIO as GPIO
import time

# Configuration des broches du capteur
pin_capteur = 17  # Remplacez 17 par le numéro de la broche que vous utilisez

# Configuration des broches du Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_capteur, GPIO.IN)

try:
    while True:
        if GPIO.input(pin_capteur) == GPIO.LOW:
            print("Obstacle détecté!")
        else:
            print("Pas d'obstacle détecté.")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
