import Adafruit_GPIO.I2C as I2C 	# Implementation APIs to read/write I2C registers 
import sensor_info			# contains list of sensor addresses and corresponding information
import smbus_scan			# function to scan i2c bus and returs list of connected sensors
import time
import sys


""" return : List of i2c devices connected to i2c-1 bus
"""
def detectall():
	return smbus_scan.scan_i2c_bus()

	
""" 	device_addr : i2c device address
	return      : information about device i.e., name, important registers
"""	
def getinfo(device_addr):
	if device_addr in sensor_info.device_dictionary:
		return sensor_info.device_dictionary[device_addr]			
	else:
		return "No information available"
		

"""	device_addr : i2c device address
	register    : register of <device_addr> from which data to be read
	return      : read data
"""
def readfrom(device_addr,register):
	try:
		device = I2C.get_i2c_device(device_addr)
		ans = device.readU8(register)
		return ans
	except IOError:
		return "No Device Found"


"""	device_addr : i2c device address
	register    : register of <device_addr> into which data to be written
"""
def writeto(device_addr,register,value):
	try:
		device = I2C.get_i2c_device(device_addr)
		device.write8(register,value)
	except IOError:
		return "No Device found"




##This is for debugging
	
"""print("This is debugging")
print(detectall())

for i in range(1,5):
	command		= raw_input('Command:')
	if command == "quit":
		break

	device_addr     = raw_input('Device address:')
        reg_addr        = raw_input('Register address:')
	if command == 'writeto':
		data 	= raw_input('write Data:')
		writeto(int(device_addr),int(reg_addr),int(data))
	
	print(readfrom(int(device_addr),int(reg_addr)))"""
		                
