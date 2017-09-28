#############################################################################################################
		## library dependencies
import bluetooth
import subprocess
import ast
import sensor_top


############################################################################################################
		## Global variables

RxBuffSize = 4096
BTPortNo = 3
ServerOn = 1
client = ''
connected = 0

############################################################################################################
		## functions and utilities

#make the bluetooth device discoverable (onlt in chip)
subprocess.call(['sudo','hciconfig','hci0','piscan'])

def detectall(x): # detectall command
	data = sensor_top.detectall()
	TxData = '[\"'+data+'\"]'
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass

def getinfo(x): # getinfo command
	data = sensor_top.getinfo(x[1])
	TxData = '[\"'+data+'\"]'
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass

def readfrom(x):
	print("readfrom::",x,x[1],x[2])
	data = sensor_top.readfrom(x[1],x[2])
	print(data)
	TxData = '[\"'+str(data)+'\"]'
	print(TxData)
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass

def writeto(x):
	sensor_top.writeto(x[1],x[2],x[3])
	TxData = '[\"write successfull\"]'
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass

def quit__():
	client.close()
	


###########################################################################################################
		## command dictionary to lookup
command_dictionary = {	"detectall"	: detectall, \
			#"initialize"	: initialize, \
			"getinfo"	: getinfo, \
			"readfrom"	: readfrom, \
			"writeto"	: writeto, \
			"quit"		: quit__
		     }


###########################################################################################################
		## main function/ code

if __name__ == "__main__":

	print("Starting server...")
	#create bluetooth socket and acept connection from master
	server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	server.bind(("",BTPortNo))
	server.listen(1)
	try:
		while(1):
			print("Waiting for connection from master [RFCOMM port=%d]" % BTPortNo)
			client,client_info = server.accept()
			print("Connected to",client_info)
			#send/recieve to/from master
			try:
				while True:
					RxData = client.recv(RxBuffSize)
					RxData = ast.literal_eval(RxData)
					print("Recieved command:",RxData)	
					command_dictionary[RxData[0]](RxData)

			#handle exceptions/ctrl + c
			except KeyboardInterrupt:
				print("Shutting down...")
				client.close()
				server.close()
			except:
				client.close()
	except KeyboardInterrupt:
		print("Shuttig down...")
		client.close()
		server.close()		
	except:
		print("exit")
		client.close()
		server.close()
