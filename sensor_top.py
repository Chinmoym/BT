import Adafruit_GPIO.I2C as I2C
import sensor_trial
import time
import sys


def detectall():
	device_addr = 0x77
	return device_addr

def getinfo(addr):
	if addr is 0x77:
		sensor1 = sensor_trial.BMP085()
		return sensor1.info

def read_from(device_addr,register):
	if device_addr is 0x77:
		device = I2C.get_i2c_device(device_addr)
		ans = device.readU8(register)
		return ans

def write_to(device_addr,register,value):
	if device_addr is 0x77:
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
