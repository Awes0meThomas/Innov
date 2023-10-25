import neopixel
import board

NUM_LEDS = 144
DATA_PIN = board.D21

# Initialise la bibliothèque ws281x
strip = neopixel.NeoPixel(DATA_PIN, NUM_LEDS, auto_write=True)

try:
    # Code pour contrôler les LEDs
    # Allumez la LED en rouge
    strip.fill((255, 0, 0))
    
    # Ajoutez ici d'autres opérations pour contrôler vos LEDs si nécessaire
    
finally:
    # Assurez-vous de libérer les ressources, même en cas d'erreur
    strip.deinit()
