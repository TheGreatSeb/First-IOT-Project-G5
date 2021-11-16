#Under her ser vi alt det som vi importere til koden, det kan være Ffx. være Pin eller time. Men vi importere også vores egne filer som vi har lavet, som buzzer og credentials.  
import credentials 
import umqtt_robust2
import GPSfunk
from machine import Pin
from time import ticks_ms, sleep_ms, sleep
import time
import neopixel, dht
import lightAnimations
import buzzer
import _thread
import os
lib = umqtt_robust2

#Nedeunder her definere vi interval og state og previoustime som bruges til vores non blocking delays. 
dht11_interval = 15000
dht11_state = 0
dht11_previousTime = 0
preivousTemp = 0
intervalTemp = 10000
sensor = dht.DHT11(Pin(26))
redon = 0 # her definere vi redon til altid at være 0 når den starter. 

#nedeunder her, definere vi de feeds som vi også bruger i adafruit. Vi skriver brugernavnet og navnet på det feed i () som vi gerne vil have koden skal connecte til når vi skriver det defineret navn.   
mapFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'mapfeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
speedFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'speedfeed/csv'), 'utf-8')
temperatureFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'temperaturefeed/csv'), 'utf-8')
# opret en ny feed kaldet speed_gps indo på io.adafruit
humidityFeed = bytes('{:s}/feeds/{:s}'.format(b'Anas0418', b'humidityfeed/csv'), 'utf-8')

while True: 
    current_time = ticks_ms() #her definere vi current_time til at være ticks_ms(). 
    if (current_time - dht11_previousTime > dht11_interval): #her starter vi en if sætning, og skriver, CT - dht11_PT er større end dht11 interval så starter vi vores loop også køre alt nedeunder. 
        try:
            dht11_previousTime = current_time # her siger vi at dht11 er lig med current_time for at trække ticks ned af...
            sensor.measure() # Denne sætning fortæller koden og deviceen at den skal måle de sensorer som vi har sat til. 
            temp = sensor.temperature() # her definere vi en af vores sensorer som temp, som svare til sensor.temperature
            hum = sensor.humidity() #vi gør det samme her bare hum istedet. 
            print("temperature: %3.1f C" % temp) # her fortæller vi den at den skal printe tempertature som svare til den ligning. 
            print("Hum: %3.1f" %  hum) #gør det samme her bare med hum
        except OSError:
            print("DHT sensor fejlede")
        if (temp < 25 and hum < 60): # her starter vi endnu en if sætning hvor her siger vi hvis temp er større end 25 og hum er større end 60 så skal den køre koden nedeunder. 
            _thread.start_new_thread(lightAnimations.clear, ()) # her starter vi en thread som indholder vores light animations som så her er clear så den lyser ikke.
            redon = 0 # redon  er 0 i denne statement, hvilket bare fortæller os at den røde light er slukket.
            buzzer.set_buzbuz_off() # her referere vi til vores fil buzzer. og fortæller den at buzzeren skal være slukket
            print("Lys: Clear") 
        elif (temp < 30 and hum < 70): # her laver vi en elif som er en hvis den før ikke rammer de tal og de rammer disse så køre den koden nedenfor, og her er det hvis temp er større end 30 osv...
            _thread.start_new_thread(lightAnimations.yellowCycle, (255, 155, 0, 50)) # her starter vi også en thread her skriver vi den skal lyse yellow ved at bruge r,g,b colors. 
            redon = 0 # igen er rød slukket
            buzzer.set_buzbuz_off() # og buzzer er også slukket 
            print("Lys: Yellow")
        elif (temp < 40 and hum < 100): #igen her siger vi hvis ikke de andre tal men disse tal så sker koden nedenfor. 
            _thread.start_new_thread(lightAnimations.redCycle, (255, 0, 0, 50)) #starter en ny thread som indeholder animations og r,g,b talene til farven rød.
            if redon == 0: #her skriver vi en ny if sætning som siger at rød skal være 0 før at buzzeren tænder, som betyder at den kan ikke køre vores loop om og hvis det røde lys stadig er tændt, så er redon = 1 og så skal buzzeren  
                buzzer.set_buzbuz_on() # her fortæller vi at buzzeren skal være tændt. 
                time.sleep(1)
                buzzer.set_buzbuz_off() # her siger vi at efter 1 sek, hvor buzzeren har været tændt skal den slukke.
                redon = 1 # her er redon = 1 da buzzeren har været tændt, så hvis loopen bliver kørt igen og de røde lys stadig er tændt så starter buzzeren ikke igen før den har været en anden farve. 
            print("Lys: Red")
        if lib.c.is_conn_issue():
            while lib.c.is_conn_issue():
                #hvis der forbindes returnere is_conn_issue metoden ingen fejlmeddelse
                lib.c.reconnect()
                print("reconnect")
            else:
                lib.c.resubscribe()
        try: # her laver vi en try inden i vores while lykke som har vores puplish kode. 
            lib.c.publish(topic=mapFeed, msg=GPSfunk.main()) #her fortæller vi den at den skal puplish vores data fra Gpsfunk filen til mapfeed inden på adafruit.io 
            speed = GPSfunk.main() # her siger vi at den også skal have speed data fra vores gpsfunk fil
            speed = speed[:4]
            print("speed: ", speed)
            lib.c.publish(topic=speedFeed, msg=str(speed)) # her fortæller vi den at den skal puplish vores data til et andet feed vi har som hedder speedfeed
            
            currentTime = ticks_ms() # her bruger vi igen non blocking delay.
            if currentTime - preivousTemp > intervalTemp:
                preivousTemp = currentTime
                lib.c.publish(topic= temperatureFeed, msg=str(temp)) # Her gør vi det sammen som oven over, vi puplisher vores data til vores temperatur feed på adafruit. 
                print("temp: ", temp)
                lib.c.publish(topic=humidityFeed, msg=str(hum)) # og det samme her. 
                print("hum:", hum)
            
            
        except KeyboardInterrupt: # her laver vi en keyboard interrupt hvor når vi trykker på ctrl.c
            buzzer.set_buzbuz_off()
            print('Ctrl-C pressed...exiting')
            lib.c.disconnect()
            lib.wifi.active(False)
            lib.sys.exit()
     
