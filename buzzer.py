from machine import Pin
import time

buzbuz = Pin(14, Pin.OUT)

def set_buzbuz_on():
    buzbuz.value(1)
    print("BUZZ ONNN")
def set_buzbuz_off():
    buzbuz.value(0)

