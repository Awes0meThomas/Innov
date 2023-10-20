import RPi.GPIO as GPIO
import time

# Configuration des broches du capteur infrarouge et du servo moteur
IR_SENSOR_PIN = 19  # Remplacez par le numéro de la broche du capteur infrarouge
SERVO_PIN = 18      # Remplacez par le numéro de la broche du servo moteur

# Configuration du servo moteur
PWM_FREQUENCY = 50  # Fréquence PWM en Hz
DUTY_CYCLE_START = 2.5  # Cycle de service initial (angle de 0 degrés)
DUTY_CYCLE_END = 12.5   # Cycle de service final (angle de 180 degrés)
PWM_FREQUENCY = 50
DUTY_CYCLE_START = 2.5
DUTY_CYCLE_END = 12.5

# Configuration du GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Configuration du PWM pour le servo moteur
pwm = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)

object_detected = False

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH and not object_detected:
            print("Objet détecté !")
            time.sleep(1)  # Attendre 1 seconde
            pwm.start(DUTY_CYCLE_START)  # Tourner de 70 degrés (angle de départ)  # Attendre 1 seconde
            pwm.ChangeDutyCycle(DUTY_CYCLE_END)  # Retourner à la position d'origine (angle de 0 degrés)  # Attendre 1 seconde
            pwm.ChangeDutyCycle(DUTY_CYCLE_START)  # Réinitialiser la position (angle de départ)
            object_detected = True

            # Attendre 1 seconde
            time.sleep(1)

            # Tourner de 70 degrés (angle de départ)
            pwm.start(DUTY_CYCLE_START)
            time.sleep(1)

            # Retourner à la position d'origine (angle de 0 degrés)
            pwm.ChangeDutyCycle(DUTY_CYCLE_END)
            time.sleep(1)

            # Réinitialiser la position (angle de départ)
            pwm.ChangeDutyCycle(DUTY_CYCLE_START)
            object_detected = False
        else:
            time.sleep(3)  # Attendre un court instant avant de vérifier à nouveau
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Nettoyage des broches GPIO et arrêt du PWM
pwm.stop()
GPIO.cleanup()
