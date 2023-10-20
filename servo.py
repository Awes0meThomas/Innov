import RPi.GPIO as GPIO
import time

IR_EMITTER_PIN = 17  
PHOTODETECTOR_PIN = 19  
SERVO_PIN = 17  

PWM_FREQUENCY = 50
DUTY_CYCLE_START = 2.5
DUTY_CYCLE_END = 12.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_EMITTER_PIN, GPIO.OUT)
GPIO.setup(PHOTODETECTOR_PIN, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, PWM_FREQUENCY)

object_detected = False
laser_on = True  

try:
    while True:
     
        GPIO.output(IR_EMITTER_PIN, GPIO.HIGH if laser_on else GPIO.LOW)
        
        
        if GPIO.input(PHOTODETECTOR_PIN) == GPIO.LOW and not object_detected:
            print("Objet détecté !")
            object_detected = True
            laser_on = False  

            
            time.sleep(1)

            
            pwm.start(DUTY_CYCLE_START)
            time.sleep(1)

           
            pwm.ChangeDutyCycle(DUTY_CYCLE_END)
            time.sleep(1)

            
            pwm.ChangeDutyCycle(DUTY_CYCLE_START)
            object_detected = False
            laser_on = True  

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
