# Write your code here :-)
# Write your code here :-)
import time
import board
import neopixel
import random


pixel_pin = board.D5
num_pixels = 60
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

for i in range(num_pixels):
    r = randint(255)
    g = randint(255)
    b = randint(255)
    pixels[i] = (r,g,b)




