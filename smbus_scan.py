#This function scans i2c bus i2c-1 and
#gives returs list of devices connected to it.

from smbus2 import SMBus
import sys

# Open i2c bus 1 and read one byte from address 80, offset 0

def scan_i2c_bus():
        bus = SMBus(1)
        L = []
        for i in range(30,127):
                try:
                        b = bus.read_byte(i)
                        L.append(i)
                except IOError:
                        continue

        bus.close()
        return L

###This is for debugging
#print(scan_i2c_bus())
