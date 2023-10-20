import RPi.GPIO as GPIO
import time
from gpiozero import Servo

# Configuration des broches pour le capteur infrarouge et le servomoteur
capteur_infrarouge_pin = 19  # Remplacez par le numéro de la broche de votre capteur IR
servomoteur_pin = 18         # Remplacez par le numéro de la broche de votre servomoteur

# Initialisation de la bibliothèque GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(capteur_infrarouge_pin, GPIO.IN)

# Configuration du servomoteur
servo = Servo(servomoteur_pin)

objet_detecte = False

try:
    while True:
        if GPIO.input(capteur_infrarouge_pin) and not objet_detecte:
            objet_detecte = True
            print("Objet détecté")
            time.sleep(1)  # Attendez 1 seconde

            # Tourner le servomoteur de 70 degrés
            servo.value = 0.5
            time.sleep(1)
            servo.value = 0  # Revenir à la position de base (0 degré)
            objet_detecte = False  # Réinitialisez l'état de détection

except KeyboardInterrupt:
    pass

# Nettoyer et réinitialiser les broches GPIO
GPIO.cleanup()
