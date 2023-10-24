import RPi.GPIO as GPIO
import time

# Configuration des broches du capteur
pin_capteur = 17  # Remplacez 17 par le numéro de la broche que vous utilisez

# Configuration des broches du Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_capteur, GPIO.IN)

# Configuration des broches du servo moteur
pin_servo = 18  # Remplacez 18 par le numéro de la broche que vous utilisez
GPIO.setup(pin_servo, GPIO.OUT)

# Configuration du PWM pour le servo moteur
pwm = GPIO.PWM(pin_servo, 50)  # Fréquence de 50 Hz
pwm.start(0)

def tourner_servo(angle):
    duty_cycle = 2.5 + (12.5 - 2.5) * angle / 180.0
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)

try:
    while True:
        if GPIO.input(pin_capteur) == GPIO.LOW:
            print("Obstacle détecté!")
            time.sleep(1)
            tourner_servo(70) 
            time.sleep(1)            # Tourne le servo de 70 degrés
            tourner_servo(0) 
            time.sleep(1)       #  Reviens à la position initiale
        else:
            print("Pas d'obstacle détecté.")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
