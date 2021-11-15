from machine import Pin

buzbuz = (Pin(14), Pin.OUT)

def buzbuz(s):
    if s == 1:
        buzbuz.value(1)
    else:
        buzbuz.value(0)
