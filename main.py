from machine import Pin, TouchPad
from time import ticks_ms, sleep_ms, time
import time
"""
from redLight import *
from yellowLight import *
from greenLight import *
"""
touch_pin_gul = TouchPad(Pin(4))
#touch_pin_grøn = TouchPad(Pin(5))
#touch_pin_rød = TouchPad(Pin(16))

while True:
    if (touch_pin_gul.read() < 200):
        from yellowLight import *
    #if (touch_pin_rød.read() < 200):
    #    from redLight import *
    #if (touch_pin_grøn.read() < 200):
    #    from greenLight import *
"""
if val == 1:
    print("Starter det grønne lys")
    from greenLight import *
if val == 2:
    print("Starter det gule lys")
    from yellowLight import *
if val == 3:
    print("Starter det røde lys")
    from redLight import *
    """
