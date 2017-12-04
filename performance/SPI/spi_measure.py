from spi_top import *
from subprocess import Popen as call
from time import time
from os import nice


spi=SPI_configure()
to_send_adc_ch0=[0xD0,0x00]		#Transfer from adc channel-0
##########################................0%CPU.................############################

filename = "_0_20n"
f = open(filename,"w+")
print(nice(-20))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()



filename = "_0_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_0_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()


filename = "_0_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_0_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()



##########################...............50%CPU.................############################
call(['python','_50.py','&'])


filename = "_50_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()




filename = "_50_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_50_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()


filename = "_50_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_50_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()




##########################...............90%CPU.................############################
call(['python','_90.py','&'])


filename = "_90_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()




filename = "_90_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
	t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_90_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()


filename = "_90_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_90_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

##########################...............100%CPU.................############################
call(['python','_100.py','&'])


filename = "_100_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()




filename = "_100_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_100_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
    	t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()


filename = "_100_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()

filename = "_100_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
	t1 = time()
        SPI_transfer(spi,to_send_adc_ch0)
        t2 = time()
        tf = t2-t1
        f.write("%f|" %tf)
f.close()



