from machine import Pin
from time import sleep, ticks_ms
import dht

dht11_interval = 2000
dht11_state = 0
dht11_previousTime = 0
sensor = dht.DHT11(Pin(26))

while True:
    current_time = ticks_ms()
    print(current_time - dht11_previousTime)
    if (current_time - dht11_previousTime > dht11_interval):
        dht11_previousTime = current_time
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("temperature: %3.1f C" % temp)
        print("Hum: %3.1f" %  hum)

        
