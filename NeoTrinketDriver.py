import smbus
import time
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
class NeoTrinketDriver:
    def __init__(self):
        self.address = 0x04
    
    def setAddress(self, value):
        self.address = value
        
    def setStripLength(self, value):
        asciiListToSend = [ord(c) for c in str(value)]
        #print("setStripLength = " + str(asciiListToSend))
        bus.write_i2c_block_data(self.address, ord("a"), asciiListToSend)

    def setBrightness(self, value):
        asciiListToSend = [ord(c) for c in str(value)]
        #print("setBrightness = " + str(asciiListToSend))
        bus.write_i2c_block_data(self.address, ord("b"), asciiListToSend)

    def setPixelColor(self, index, r, g, b):
        value = str(index) + "," + str(r).zfill(3) + "," + str(g).zfill(3) + "," + str(b).zfill(3)
        asciiListToSend = [ord(c) for c in str(value)]
        #print("setPixelColorsetStripLength value = " + str(value))
        #print("setPixelColorsetStripLength = " + str(asciiListToSend))
        success = False
        while (success != True):
            try:
                bus.write_i2c_block_data(self.address, ord("c"), asciiListToSend)
                success = True
            except:
                print(str(index))
                time.sleep(.002)
                success = False

    def off(self):    
        asciiListToSend = [ord(c) for c in "off"]
        bus.write_i2c_block_data(self.address, ord("d"), asciiListToSend)


