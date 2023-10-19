import RPi.GPIO as GPIO
import time

IR_SENSOR_PIN = 8  
SERVO_PIN = 18      

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

           
            time.sleep(1)

            
            pwm.start(DUTY_CYCLE_START)
            time.sleep(1)

           
            pwm.ChangeDutyCycle(DUTY_CYCLE_END)
            time.sleep(1)

           
            pwm.ChangeDutyCycle(DUTY_CYCLE_START)
            object_detected = False
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
