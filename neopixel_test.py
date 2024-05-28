"""CircuitPython NeoPixel tester"""
import time
import board
import neopixel
from rainbowio import colorwheel

NUM_PIXELS = 160
BRIGHTNESS = 0.5

pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS, auto_write=False)
pixels.brightness = BRIGHTNESS

def rainbow(color_index):
    for i in range(NUM_PIXELS):
        pixel_index = (i * 256 // NUM_PIXELS) + color_index
        pixels[i] = colorwheel(pixel_index & 0xff)
    pixels.show()

def main():
    index = 0
    while True:
        index += 1
        index &= 0xff
        rainbow(index)

main()
