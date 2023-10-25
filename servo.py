import time
import board
import neopixel
import RPi.GPIO as GPIO

# Set up servo motor
def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False
    start = 4
    end = 12.5
    ratio = (end - start) / 180
    angle_as_percent = angle * ratio
    return start + angle_as_percent

# Using BCM pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwm_gpio = 18  # Change this to the BCM pin number
frequency = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequency)

# Set up neopixel
NUM_LEDS = 144
DATA_PIN = board.D21  # Change this to the BCM pin number
DELAY_MS = 50
BUTTON_PIN = 2  # Change this to the BCM pin number

pixels = neopixel.NeoPixel(DATA_PIN, NUM_LEDS, auto_write=False)

# Function to check if the servo motor is moving
def is_servo_moving():
    # Add code to check if the servo motor is moving
    pass

# Function for the main loop
def loop():
    error = 0  # Initialize error as 0

    # Add code to check if the servo motor is moving and update the error accordingly
    if is_servo_moving():
        error = 1
    else:
        error = 0

    if error == 2:
        for i in range(NUM_LEDS):
            pixels[i] = (0, 255, 0)  # Green
        pixels.show()
        time.sleep(0.2)
        pixels.fill((0, 0, 0))  # Turn off all LEDs
        pixels.show()
        time.sleep(0.2)
    elif error == 1:
        for i in range(NUM_LEDS):
            pixels[i] = (255, 0, 0)  # Red
        pixels.show()
        time.sleep(0.2)
        pixels.fill((0, 0, 0))  # Turn off all LEDs
        pixels.show()
        time.sleep(0.2)
    else:
        for color in range(256):
            for i in range(NUM_LEDS):
                pixels[i] = (color, 255, 255)  # Change the hue
            pixels.show()
            time.sleep(DELAY_MS / 1000)  # Convert to seconds

try:
    pwm.start(angle_to_percent(0))
    for _ in range(5):
        loop()
        time.sleep(1)

    while True:
        loop()

except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
