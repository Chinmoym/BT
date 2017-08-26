import Adafruit_GPIO.I2C as I2C
import sensor_trial
import time
import sys

def get_addr(device_name):	
	return 0x77

def detectall():
	device = 'BMP085'
	return device

def getinfo(device_name):
	sensor = device_mame.info()
	#sensor = sensor_trial.BMP085()
	return sensor

def read_from(device_name,register):
	device_addr = get_addr(device_name)
	device = I2C.get_i2c_device(device_addr)
	ans = device.readU8(register)
	return ans

def write_to(device_name,register,value):
	device_addr = get_address(device_name)
	device = I2C.get_i2c_device(device_addr)
	device.write8(register,value)


def get_temperature(device_addr = 0x77):
	if device_addr is 0x77:
		sensor1 = sensor_trial.BMP085()
		a = sensor1.read_temperature()
		return a

def get_pressure(device_addr= 0x77):
	if device_addr is 0x77:
		sensor1 = sensor_trial.BMP085()
		a = sensor1.read_pressure()
		return a
