#This function scans i2c bus i2c-1.

from smbus2 import SMBus
import sys

"""return : List of i2c devices connected to i2c-1 bus.
"""
def scan_i2c_bus():
        bus = SMBus(1)
        L = []
        for i in range(3,127):
                try:
                        b = bus.read_byte(i)
                        L.append(i)
                except IOError:
                        continue

        bus.close()
        return L

###This is for debugging
#print(scan_i2c_bus())
