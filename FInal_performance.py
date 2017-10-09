import subprocess
from time import sleep

for i in range(100):
	print "\n\n\n"
	print i
	print "\n"
	subprocess.call(['sudo','python','bt_Client_performance.py'])
	i+=1
	sleep(2)