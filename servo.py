import RPi.GPIO as GPIO
import time

# Définition des broches GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)  # Capteur infrarouge
GPIO.setup(18, GPIO.OUT)  # Servomoteur

# Définition de la fonction de rotation du servomoteur
def rotate_servo(angle):
    GPIO.output(18, True)
    time.sleep(angle / 180)
    GPIO.output(18, False)

# Boucle principale
while True:
    # Lecture du capteur infrarouge
    if GPIO.input(19) == GPIO.HIGH:
        # Si un objet est détecté, rotation du servomoteur
        rotate_servo(70)
        time.sleep(1)
        rotate_servo(0)

    time.sleep(0.1)
