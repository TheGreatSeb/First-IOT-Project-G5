from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(26))
while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        print("temperature: %3.1f C" % temp)
    except OSError:
        print('Failed to read sensor.')