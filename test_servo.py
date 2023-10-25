import neopixel
import board

NUM_LEDS = 144
DATA_PIN = board.D21  # Assurez-vous que c'est le bon pin

pixels = neopixel.NeoPixel(DATA_PIN, NUM_LEDS, auto_write=True)

# Allumez la LED en rouge
pixels.fill((255, 0, 0))
