from machine import Pin, ADC

from time import sleep

sensor = ADC(Pin(39))



while True:

    sensor_val = sensor.read()

    print("it be moistn or wet",sensor_val)

    sleep(0.1)

    

