import Adafruit_GPIO.I2C as I2C 	# Implementation APIs to read/write I2C registers 
import sensor_info			# contains list of sensor addresses and corresponding information
import smbus_scan			# function to scan i2c bus and returs list of connected sensors
import time
import sys


def detectall():
	return smbus_scan.scan_i2c_bus()
	

def getinfo(device_addr):
	if device_addr in sensor_info.device_dictionary:
		return sensor_info.device_dictionary[device_addr]
	else:
		return "Device Not Found"

"""def initialize(device_addr):
	device_name = get_name(device_addr)
	sensor = getattr(sensor_trial,device_name)		#This will initialize the device by loading default calibration
	return sensor"""

def readfrom(device_addr,register):
	try:
		device = I2C.get_i2c_device(device_addr)
		ans = device.readU8(register)
		return ans
	except IOError:
		return "No Device Found"

def writeto(device_addr,register,value):
	try:
		device = I2C.get_i2c_device(device_addr)
		device.write8(register,value)
	except IOError:
		return "No Device found"




##This is for debugging
"""print(detectall())

print(getinfo(119))
time.sleep(1)


print(readfrom(0x77,0xF4))
time.sleep(0.5)

writeto(0x77,0xF4,0x2E)
time.sleep(0.5)

for i in range(1,5):
	print('------------------')
	writeto(0x77,0xF4,0x2E)
	print(readfrom(0x77,0xF6))
	time.sleep(0.5)
	writeto(0x77,0xF4,0x01)
        print(readfrom(0x77,0xFF))
        time.sleep(0.5)"""
		

