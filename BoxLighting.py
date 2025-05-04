#This file will be used on an ESP32C3 or similar using neopixel and machine libraries
from neopixel import NeoPixel
from machime import Pin
from time import sleep

#Configuration
PIXEL_COUNT = 21
LED_PIN = 10

#Pin Definitions
neo_leds = Pin(LED_PIN, Pin.OUT)
pix = NeoPixel(neo_leds, PIXEL_COUNT) 

#function to activate all pixels
def all_pix(color):
  for p in range(PIXEL_COUNT):
    pix[p] = color
  pix.write()

#function to activate single pixel
def single_pix(color, index):
  pix[index] = color
  pix.write()

def pix_group(color, start, end):
  for p in range(start, end):
    pix[p] = color
  pix.write()
