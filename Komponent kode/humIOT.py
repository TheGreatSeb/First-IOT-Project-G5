from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(26))
while True:
    try:
        sleep(2)
        sensor.measure()
        #temp = sensor.temperature() * ( 9/5) +32.0
        #print('Temperatur: %3.1f F'%temp)
        hum = sensor.humidity()
        print('humidity %3.1f' %hum)
    except OSError as e:
        print('Failed to read sensor.')