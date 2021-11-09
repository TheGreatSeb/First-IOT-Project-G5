from machine import Pin, TouchPad
from time import ticks_ms, sleep_ms, time
import wifiConnect
import time
import neopixel
import lightAnimations
lib = wifiConnect

touch_pin_green = TouchPad(Pin(2))
touch_pin_yellow = TouchPad(Pin(4))
touch_pin_red = TouchPad(Pin(12))

while True:
    if (touch_pin_green.read() < 200):
        lightAnimations.greenCycle(0, 255, 0, 50)
    elif (touch_pin_yellow.read() < 200):
        lightAnimations.yellowCycle(255, 155, 0, 50)
    elif (touch_pin_red.read() < 200):
        lightAnimations.redCycle(255, 0, 0, 50)
    else:
        lightAnimations.offline(2, 2, 2, 50)