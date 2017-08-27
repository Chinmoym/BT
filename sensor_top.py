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
	sensor = getattr(sensor_trial,device_name)		#This will return device information
	return sensor.info

def initialize(device_name):
	sensor = getattr(sensor_trial,device_name)		#This will initialize the device by loading default calibration
	return sensor

def read_from(device_name,register):
	device_addr = get_addr(device_name)
	device = I2C.get_i2c_device(device_addr)
	ans = device.readU8(register)
	return ans

def write_to(device_name,register,value):
	device_addr = get_addr(device_name)
	device = I2C.get_i2c_device(device_addr)
	device.write8(register,value)


def get_temperature(device_name= 'BMP085'):
	device_addr = get_addr(device_name)
	if device_addr is 0x77:
		sensor1 = sensor_trial.BMP085()
		a = sensor1.read_temperature()
		return a

def get_pressure(device_name='BMP085'):
	device_addr = get_addr(device_name)
	if device_addr is 0x77:
		sensor1 = sensor_trial.BMP085()
		a = sensor1.read_pressure()
		return a


##This is for debugging

"""print(getinfo('BMP085'))
time.sleep(1)
print(initialize('BMP085'))
time.sleep(1)

print(read_from('BMP085',0xF4))
time.sleep(0.5)

write_to('BMP085',0xF4,0x2E)
time.sleep(0.5)

for i in range(1,10):
	print('------------------')
	write_to('BMP085',0xF4,0x2E)
	print(read_from('BMP085',0xF7))
	time.sleep(0.5)
	write_to('BMP085',0xF4,0x34)
        print(read_from('BMP085',0xF7))
        time.sleep(0.5)"""
		


