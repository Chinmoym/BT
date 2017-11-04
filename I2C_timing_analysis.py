from sensor_top import *
from subprocess import Popen as call
from time import time
from os import nice

device = 0x77
rd_reg = 0xF6
wt_reg = 0xF4
wt_val  = 0x34

##########################................0%CPU.................############################

filename = "_0_20n"
f = open(filename,"w+")
print(nice(-20))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()



filename = "_0_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_0_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()


filename = "_0_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_0_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()



##########################...............50%CPU.................############################
call(['python','_50.py','&'])


filename = "_50_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()




filename = "_50_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_50_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()


filename = "_50_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_50_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()




##########################...............90%CPU.................############################
call(['python','_90.py','&'])


filename = "_90_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()




filename = "_90_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_90_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()


filename = "_90_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_90_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

##########################...............100%CPU.................############################
call(['python','_100.py','&'])


filename = "_100_20n"
f = open(filename,"w+")
print(nice(-40))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()




filename = "_100_10n"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_100_0"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()


filename = "_100_10"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()

filename = "_100_20"
f = open(filename,"w+")
print(nice(10))
for i in range(0,1000):
        t1 = time()
        detectall()
        t2 = time()
        readfrom(device,rd_reg)
        t3 = time()
        writeto(device,wt_reg,wt_val)
        t4 = time()
        da = t2-t1
        rf = t3-t2
        wt = t4-t3
        f.write("%f|" %da)
        f.write("%f|" %rf)
        f.write("%f\n" %wt)
f.close()


