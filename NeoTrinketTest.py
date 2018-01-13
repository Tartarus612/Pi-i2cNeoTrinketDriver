import NeoTrinketDriver
import time
import random

myDriver = NeoTrinketDriver.NeoTrinketDriver()
myDriver.setAddress(0x04)
myDriver.setStripLength(144)
time.sleep(.06)
myDriver.setBrightness(10)
time.sleep(.06)
index = 0
r = 255
g = 255
b = 255
while(True):
    if(index == 144):
        index = 0
    r = random.randrange(15, 255)
    g = random.randrange(15, 255)
    b = random.randrange(15, 255)
    myDriver.setPixelColor(index, r, g, b)
    index = index + 1
    time.sleep(.006)