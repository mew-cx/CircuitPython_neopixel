# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from rainbowio import colorwheel
import neopixel

PIXEL_PIN = board.MOSI
NUM_PIXELS = 12

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, auto_write=False)

def color_chase(num_pixels, color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

def rainbow_cycle(num_pixels, wait):
    STEPS = 256
    for j in range(STEPS-1):
        for i in range(num_pixels):
            rc_index = (i * STEPS // num_pixels) + j
            pixels[i] = colorwheel(rc_index & STEPS-1)
        pixels.show()
        time.sleep(wait)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(2)

    pixels.fill(WHITE)
    pixels.show()
    time.sleep(3)

    pixels.fill(RED)
    pixels.show()
    time.sleep(1)

    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)

    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    delay = 0.02
    color_chase(NUM_PIXELS, RED, delay)
    color_chase(NUM_PIXELS, YELLOW, delay)
    color_chase(NUM_PIXELS, GREEN, delay)
    color_chase(NUM_PIXELS, CYAN, delay)
    color_chase(NUM_PIXELS, BLUE, delay)
    color_chase(NUM_PIXELS, PURPLE, delay)
    color_chase(NUM_PIXELS, BLACK, delay)

    rainbow_cycle(NUM_PIXELS, 0.005)

    pixels.fill(BLACK)
    pixels.show()
    time.sleep(0.5)

    rainbow_cycle(NUM_PIXELS, 0.001)
