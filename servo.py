import RPi.GPIO as GPIO
import time

IR_SENSOR_PIN = 17  # Remplacez par le numéro de la broche du capteur infrarouge
SERVO_PIN = 18  # Remplacez par le numéro de la broche du servo moteur

PWM_FREQUENCY = 50
DUTY_CYCLE_START = 2.5
DUTY_CYCLE_END = 12.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)

object_detected = False

try:
    while True:
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH and not object_detected:
            print("Objet détecté !")
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
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
