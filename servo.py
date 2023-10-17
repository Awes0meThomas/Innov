import RPi.GPIO as GPIO
import time
from gpiozero import Servo


IR_PIN = 7  
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)


SERVO_PIN = 18  
servo = Servo(SERVO_PIN)

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

except KeyboardInterrupt:
    print("Arrêt du programme")

finally:
    GPIO.cleanup()
