import RPi.GPIO as GPIO
import time
from gpiozero import Servo


IR_PIN = 19  
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(23, GPIO.IN)  
GPIO.setup(17, GPIO.OUT)  


SERVO_PIN = 18  
servo = Servo(SERVO_PIN)
def rotate_servo(angle):
    GPIO.output(17, True)
    time.sleep(angle / 180)
    GPIO.output(17, False)

try:
    while True:
       if GPIO.input(capteur):
           print ("Mouvement detecte")
           time.sleep(1)
           print("Rotation du servomoteur de 70 degrés.")
           servo.value = 0.5  
           time.sleep(1)
           print("Retour du servomoteur à la position d'origine.")
           servo.value = 0  
       else:
           time.sleep(0.1)
# Boucle principale
while True:
    # Si le capteur infrarouge détecte quelque chose
    if GPIO.input(23) == GPIO.HIGH:
        # Attendre une seconde
        time.sleep(1)

except KeyboardInterrupt:
    print("Arrêt du programme")
        # Rotation du servo moteur de 70 degrés
        rotate_servo(70)

finally:
    GPIO.cleanup()
        # Retour à la position d'origine
        rotate_servo(-70)
