from machine import Pin, PWM
import time

def buzzOn(x):
    buzzer = PWM(Pin(14), freq=10, duty=5)
    time.sleep(x)
    buzzer.duty(0)
    time.sleep(x)
