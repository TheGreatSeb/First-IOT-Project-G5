import machine, neopixel
import time

# number of pixels
n = 12
# strip control gpio
p = 15

np = neopixel.NeoPixel(machine.Pin(p), n)

def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

# green cycle
def greenCycle(r, g, b, wait):
  for i in range(1 * n):
    for j in range(n):
      np[j] = (0, 5, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

# yellow cycle
def yellowCycle(r, g, b, wait):
  for i in range(1 * n):
    for j in range(n):
      np[j] = (3, 2, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

# red cycle
def redCycle(r, g, b, wait):
  for i in range(1 * n):
    for j in range(n):
      np[j] = (5, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)
