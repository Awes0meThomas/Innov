import RPi.GPIO as GPIO
import time

# Configuration des broches du capteur infrarouge et du servo moteur
IR_SENSOR_PIN = 8  # Remplacez par le numéro de la broche du capteur infrarouge
SERVO_PIN = 18      # Remplacez par le numéro de la broche du servo moteur

# Configuration du servo moteur
PWM_FREQUENCY = 50  # Fréquence PWM en Hz
DUTY_CYCLE_START = 2.5  # Cycle de service initial (angle de 0 degrés)
DUTY_CYCLE_END = 12.5   # Cycle de service final (angle de 180 degrés)

# Configuration du GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuration du PWM pour le servo moteur
pwm = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH:
            print("Objet détecté !")
            time.sleep(1)  # Attendre 1 seconde
            pwm.start(DUTY_CYCLE_START)  # Tourner de 70 degrés (angle de départ)  # Attendre 1 seconde
            pwm.ChangeDutyCycle(DUTY_CYCLE_END)  # Retourner à la position d'origine (angle de 0 degrés)  # Attendre 1 seconde
            pwm.ChangeDutyCycle(DUTY_CYCLE_START)  # Réinitialiser la position (angle de départ)
        else:
            time.sleep(3)  # Attendre un court instant avant de vérifier à nouveau

except KeyboardInterrupt:
    pass

# Nettoyage des broches GPIO et arrêt du PWM
pwm.stop()
GPIO.cleanup()
