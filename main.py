import credentials
import umqtt_robust2
import GPSfunk
from machine import Pin
from time import ticks_ms, sleep_ms, sleep
import neopixel, dht
import lightAnimations
lib = umqtt_robust2

dht11_interval = 2000
dht11_state = 0
dht11_previousTime = 0
preivousTemp = 0
intervalTemp = 10000
sensor = dht.DHT11(Pin(26))

mapFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'mapfeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'speedfeed/csv'), 'utf-8')
temperatureFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'temperaturefeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
humidityFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'humidityfeed/csv'), 'utf-8')

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
        if lib.c.is_conn_issue():
            while lib.c.is_conn_issue():
                #hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
                lib.c.reconnect()
            else:
                lib.c.resubscribe()
        try:
            lib.c.publish(topic=mapFeed, msg=GPSfunk.main())
            speed = GPSfunk.main()
            speed = speed[:4]
            print("speed: ", speed)
            lib.c.publish(topic=speedFeed, msg=str(speed))
            
            currentTime = ticks_ms()
            if currentTime - preivousTemp > intervalTemp:
                preivousTemp = currentTime
                lib.c.publish(topic= temperatureFeed, msg=str(temp))
                print("temp: ", temp)
                lib.c.publish(topic=humidityFeed, msg=str(hum))
                print("hum:", hum)
            
            
        except KeyboardInterrupt:
            print('Ctrl-C pressed...exiting')
            lib.c.disconnect()
            lib.wifi.active(False)
            lib.sys.exit()
"""
mapFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'mapfeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'speedfeed/csv'), 'utf-8')

while True:
    if lib.c.is_conn_issue():
        while lib.c.is_conn_issue():
            # hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
            lib.c.reconnect()
        else:
            lib.c.resubscribe()
    try:
        lib.c.publish(topic=mapFeed, msg=GPSfunk.main())
        speed = GPSfunk.main()
        speed = speed[:4]
        print("speed: ",speed)
        lib.c.publish(topic=speedFeed, msg=speed)
        sleep(10) 
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.c.disconnect()
        lib.wifi.active(False)
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')
    except NameError as e:
        print('NameError')
    except TypeError as e:
        print('TypeError')
    lib.c.check_msg() # needed when publish(qos=1), ping(), subscribe()
    lib.c.send_queue()  # needed when using the caching capabilities for unsent messages

lib.c.disconnect()

"""
