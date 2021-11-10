from machine import Pin, PWM
import time

buzzer = PWM(Pin(14), freq=10, duty=5)
time.sleep(70)
buzzer.deinit()