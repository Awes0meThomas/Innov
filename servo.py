import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)  
GPIO.setup(17, GPIO.OUT)  


def rotate_servo(angle):
    GPIO.output(17, True)
    time.sleep(angle / 180)
    GPIO.output(17, False)

# Boucle principale
while True:
    # Si le capteur infrarouge détecte quelque chose
    if GPIO.input(23) == GPIO.HIGH:
        # Attendre une seconde
        time.sleep(1)

        # Rotation du servo moteur de 70 degrés
        rotate_servo(70)

        # Retour à la position d'origine
        rotate_servo(0)
