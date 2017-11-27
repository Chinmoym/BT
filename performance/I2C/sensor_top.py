#import Adafruit_GPIO.I2C as I2C
#import sensor_trial
#import smbus_scan
import time
import sys

device_dictionary =  { 0x77 : 'BMP085'
}

def get_name(dev_addr):
	return device_dictionary[dev_addr]

def detectall():
	return "smbus_scan.scan_i2c_bus()"
	

def getinfo(device_addr):
	if device_addr in device_dictionary:
		device_name = get_name(device_addr)
	#	sensor = getattr(sensor_trial,device_name)		#This will return device information
		return "sensor.info"
	else:
		return "Device Not Found"

#def initialize(device_addr):
#	device_name = get_name(device_addr)
#	sensor = getattr(sensor_trial,device_name)		#This will initialize the device by loading default calibration
#	return sensor

def readfrom(device_addr,register):
	try:
		return "ans"
	except IOError:
		return "No Device Found"

def writeto(device_addr,register,value):
	try:
		print "done"
#		device = I2C.get_i2c_device(device_addr)
#		device.write8(register,value)
	except IOError:
		return "No Device found"



##This is for debugging
"""print(detectall())
print(get_name(119))

print(getinfo(119))
time.sleep(1)
print(initialize(0x77))
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
	writeto(0x77,0xF4,0x34)
        print(readfrom(0x77,0xF6))
        time.sleep(0.5)"""
		

