from machine import Pin

buzbuz = (Pin(14), Pin.OUT)

def set_buzbuz_on():
    buzbuz.value(1)
def set_buzbuz_off():
    buzbuz.value(0)
