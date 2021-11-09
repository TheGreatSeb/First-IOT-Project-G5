from machine import Pin, TouchPad
from time import ticks_ms, sleep_ms, time
import time
import neopixel
import lightAnimations

touch_pin_green = TouchPad(Pin(2))
touch_pin_yellow = TouchPad(Pin(4))
touch_pin_red = TouchPad(Pin(12))

while True:
    if (touch_pin_green.read() < 200):
        lightAnimations.greenCycle(0, 255, 0, 50)
        lightAnimations.clear()
    elif (touch_pin_yellow.read() < 200):
        lightAnimations.yellowCycle(255, 155, 0, 50)
        lightAnimations.clear()
    elif (touch_pin_red.read() < 200):
        lightAnimations.redCycle(255, 0, 0, 50)
        lightAnimations.clear()
    else:
        lightAnimations.offline(2, 2, 2, 50)
        lightAnimations.clear()


