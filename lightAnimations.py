import machine, neopixel
import time

# number of pixels
n = 12
# strip control gpio
p = 15

np = neopixel.NeoPixel(machine.Pin(p), n)

#Clear LED's
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

#Color Cycle
def colorCycle(color, bg, wait):
  for i in range(2 * n):
    for j in range(n):
      np[i % n] = color
      np.write()
      time.sleep_ms(wait)

# green cycle
def greenCycle(r, g, b, wait):
  for i in range(2 * n):
    for j in range(n):
      np[j] = (0, 5, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

# yellow cycle
def yellowCycle(r, g, b, wait):
  for i in range(2 * n):
    for j in range(n):
      np[j] = (3, 2, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

# red cycle
def redCycle(r, g, b, wait):
  for i in range(2 * n):
    for j in range(n):
      np[j] = (5, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

# offline status
def offline(r, g, b, wait):
  for i in range(2 * n):
    for j in range(n):
      np[j] = (1, 1, 1)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)

