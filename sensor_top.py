#Implementation of functions used in bt_server.py

import Adafruit_GPIO.I2C as I2C
import sensor_trial
import smbus_scan
import time
import sys


def get_name(dev_addr):
        if dev_addr == 0x77:
                return 'BMP085'

def detectall():
        return smbus_scan.scan_i2c_bus()


def getinfo(device_addr):
        device_name = get_name(device_addr)
        sensor = getattr(sensor_trial,device_name)              #This will return device information
        return sensor.info

def initialize(device_addr):
        device_name = get_name(device_addr)
        sensor = getattr(sensor_trial,device_name)              #This will initialize the device by loading default calibration
        return sensor

def read_from(device_addr,register):
        device = I2C.get_i2c_device(device_addr)
        ans = device.readU8(register)
        return ans

def write_to(device_addr,register,value):
        device = I2C.get_i2c_device(device_addr)
        device.write8(register,value)


def get_temperature(device_addr):
        device_name = get_name(device_addr)
        sensor1 = getattr(sensor_trial,device_name)
        temperature = sensor1.read_temperature()
        return temperature

def get_pressure(device_addr):
        device_name = get_name(device_addr)
        sensor1 = getattr(sensor_trial,device_name)
        pressure = sensor1.read_pressure()
        return pressure


##This is for debugging
"""print(detectall())

print(getinfo(0x77))
time.sleep(1)
print(initialize(0x77))
time.sleep(1)

print(read_from(0x77,0xF4))
time.sleep(0.5)

write_to(0x77,0xF4,0x2E)
time.sleep(0.5)

for i in range(1,5):
        print('------------------')
        write_to(0x77,0xF4,0x2E)
        print(read_from(0x77,0xF6))
        time.sleep(0.5)
        write_to(0x77,0xF4,0x34)
        print(read_from(0x77,0xF6))
        time.sleep(0.5)"""


