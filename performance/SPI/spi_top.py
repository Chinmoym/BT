import Adafruit_GPIO.SPI as SPI				#SPI library
import CHIP_IO.OverlayManager as OM			# To load/unload SPI
import CHIP_IO.GPIO as gpio				# To configure GPIO
import time

OM.load("SPI2")			#load SPI2 


ADC_CS = "U14_32"		#GPIO Pin to be used as Chip select for SPI (here , device is 12-bit ADC MCP3202)

gpio.setup(ADC_CS,gpio.OUT)		#CS for ADC
gpio.output(ADC_CS,gpio.HIGH)		#Set as output

"""configure SPI"""
def SPI_configure():
	spi = SPI.SpiDev(2, 0, 500000)		# create a class for SPI bus2,device 0, 500kHz clock.
	spi.set_bit_order(SPI.MSBFIRST)
	spi.set_clock_hz(500000)
	spi.set_mode(0)
	return spi

""" Transfer from SPI, for full Duplex"""
def SPI_transfer(spi,send_data):
	data = [0x00,0x00]				# received data tobe stored in 'data'
	try:
		gpio.output(ADC_CS,gpio.LOW)		# Choose ADC to transfer
		data = spi.transfer(send_data)		# get 12-bit ADC data
		gpio.output(ADC_CS,gpio.HIGH)		
	except:
		print('SPI Error')
	return data

"""Write in SPI device, this will not work for ADC which we are using""" 
def SPI_write(spi,send_data):   
        try:
                gpio.output(ADC_CS,gpio.LOW)
                spi.write(send_data)
                gpio.output(ADC_CS,gpio.HIGH)
        except:
                print("SPI write Error")

"""Get data from SPI device, this will not work for ADC which we are using""" 
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
