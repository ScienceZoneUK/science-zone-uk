from adafruit_circuitplayground.express import cpx
import time

brightness = 0.0
step = 0.01

while True:
    cpx.pixels.brightness = brightness
    cpx.pixels.fill((0, 0, 255))  # Blue
    time.sleep(0.02)

    brightness += step

    if brightness >= 1.0 or brightness <= 0.0:
        step = -step  # Reverse direction
