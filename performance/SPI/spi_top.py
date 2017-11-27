import Adafruit_GPIO.SPI as SPI
import CHIP_IO.OverlayManager as OM
import CHIP_IO.GPIO as gpio
import time

OM.load("SPI2")


ADC_CS = "U14_32"

gpio.setup(ADC_CS,gpio.OUT)		#CS for ADC
gpio.output(ADC_CS,gpio.HIGH)

"""configure SPI"""
def SPI_configure():
	spi = SPI.SpiDev(2, 0, 500000)
	spi.set_bit_order(SPI.MSBFIRST)
	spi.set_clock_hz(500000)
	spi.set_mode(0)
	return spi

""" Transfer from SPI, for full Duplex"""
def SPI_transfer(spi,send_data):
	data = [0x00,0x00]
	try:
		gpio.output(ADC_CS,gpio.LOW)
		data = spi.transfer(send_data)
		gpio.output(ADC_CS,gpio.HIGH)
	except:
		print('SPI Error')
	return data

def SPI_write(spi,send_data):   
        try:
                gpio.output(ADC_CS,gpio.LOW)
                spi.write(send_data)
                gpio.output(ADC_CS,gpio.HIGH)
        except:
                print("SPI write Error")

def SPI_read(spi,bytes):
        data = []   
        try:
                gpio.output(ADC_CS,gpio.LOW)
                data = spi.read(bytes)
                gpio.output(ADC_CS,gpio.HIGH)
                return data
        except:
                return "SPI Error"



#This is for debug		
"""#to_send = [0x80,0x00]
to_send_ch0 = [0xD0, 0x00]              #11010000 
to_send_ch1 = [0xF0, 0x00]

spi = SPI_configure()

for i in range(1,20):
	if(i%2):
		data = SPI_transfer(spi,to_send_ch0)
	else:	
		data = SPI_transfer(spi,to_send_ch1)
	data[0] = 0x0F & data[0]
	print(data[0], data[1])	
	time.sleep(2)

spi.close()
OM.unload("SPI2")"""
