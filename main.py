from machine import Pin
from time import ticks_ms, sleep_ms
#import wifiConnect
import neopixel, dht
import lightAnimations
#lib = wifiConnect

dht11_interval = 2000
dht11_state = 0
dht11_previousTime = 0
sensor = dht.DHT11(Pin(26))

while True:
    current_time = ticks_ms()
    if (current_time - dht11_previousTime > dht11_interval):
        dht11_previousTime = current_time
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        print("temperature: %3.1f C" % temp)
        print("Hum: %3.1f" %  hum)
        if (temp < 25 and hum < 60):
            lightAnimations.clear
            print("Lys: Clear")
        elif (temp < 30 and hum < 70):
            lightAnimations.yellowCycle(255, 155, 0, 50)
            print("Lys: Yellow")
        elif (temp < 40 and hum < 100):
            lightAnimations.redCycle(255, 0, 0, 50)
            print("Lys: Red")
    """
    elif (touch_pin_yellow.read() < 200):
        lightAnimations.yellowCycle(255, 155, 0, 50)
    elif (touch_pin_red.read() < 200):
        lightAnimations.redCycle(255, 0, 0, 50)
    else:
        lightAnimations.offline(2, 2, 2, 50)
        """

