import machine, neopixel
import time

# number of pixels
n = 12
# strip control gpio
p = 15

np = neopixel.NeoPixel(machine.Pin(p), n)
# cycle
def cycle(r, g, b, wait):
  for i in range(40 * n):
    for j in range(n):
      np[j] = (5, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

cycle(255, 0, 0, 75)
time.sleep(1)

# turn off all pixels
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

