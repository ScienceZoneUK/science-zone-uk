# Write your code here :-)
# Write your code here :-)
import time
import board
import neopixel

# Setup NeoPixels (60 LEDs on A0)
pixel_pin = board.D5
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

pixels.fill((255 , 0, 0))
pixels.show()
