# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.A1
num_pixels = 155

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    pixels.fill(WHITE)
    pixels.show()
    time.sleep(1)

    pixels.fill(RED)
    pixels.show()
    time.sleep(1)

    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)

    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    delay = 0.01
    #color_chase(RED, delay)
    color_chase(YELLOW, delay)
    #color_chase(GREEN, delay)
    color_chase(CYAN, delay)
    #color_chase(BLUE, delay)
    color_chase(PURPLE, delay)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
