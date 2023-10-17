import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
from gpiozero import Servo

# Configurer le GPIO pour le capteur infrarouge
IR_PIN = 7  # GPIO17 (ou le numéro de votre choix)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

# Configurer le GPIO pour le servomoteur
SERVO_PIN = 18  # GPIO18 (ou le numéro de votre choix)
servo = Servo(SERVO_PIN)

try:
    while True:
       if GPIO.input(capteur):
           print "Mouvement detecte"
           time.sleep(1)
           print("Rotation du servomoteur de 70 degrés.")
           servo.value = 0.5  # Rotation du servomoteur de 70 degrés (valeur à ajuster si nécessaire)
           time.sleep(1)
           print("Retour du servomoteur à la position d'origine.")
           servo.value = 0  # Retour à la position d'origine
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Arrêt du programme")

finally:
    GPIO.cleanup()
