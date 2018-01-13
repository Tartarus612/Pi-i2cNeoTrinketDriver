import smbus
import time
import base64
# for RPI version 1, use “bus = smbus.SMBus(0)”
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    asciiListToSend = [ord(c) for c in value]
    print("asciiListToSend = " + str(asciiListToSend))
    bus.write_i2c_block_data(address, 1, asciiListToSend)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    #bytes = bus.read_i2c_block_data(address, 0, 32)
    #number = str.decode(bytes)
    number = bus.read_byte_data(address, 1)
    return number

while True:
    var = input("Enter 1 – 9: ")
    if not var:
        continue

    writeNumber(var)
    print("RPI: Hi Arduino, I sent you " + str(var))
    # sleep one second
    #time.sleep(1)

    number = readNumber()
    #print("Arduino: Hey RPI, I received a digit " + str(number))
    print

