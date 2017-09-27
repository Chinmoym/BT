#############################################################################################################
		## library dependencies
import bluetooth
import subprocess
import ast
#import sensor_top


############################################################################################################
		## Global variables

RxBuffSize = 1024
BTPortNo = 3
ServerOn = 1
client = ''

############################################################################################################
		## functions and utilities

#make the bluetooth device discoverable (onlt in chip)
#subprocess.call(['sudo','hciconfig','hci0','piscan'])

def detectall(x): # detectall command
	print(x)
	data = sensor_top.detectall()
	#TxData = '[\"'+data+'\"]'
	client.send(Data)

def getinfo(x): # getinfo command
	print (x)
	data = sensor_top.getinfo(x[1])
	client.send(data)

def readfrom(x):
	print(x)
	data = sensor_top.readfrom(x[1],x[2])
	data = format(data, '#04X')
	client.send(data)

def writeto(x):
	print(x)
	sensor_top.write_to(x[1],x[2],x[3])
	client.send("write successfull")


###########################################################################################################
		## command dictionary to lookup
command_dictionary = {	"detectall"	: detectall, \
			#"initialize"	: initialize, \
			"getinfo"	: getinfo, \
			"readfrom"	: readfrom, \
			"writeto"	: writeto\
		     }


###########################################################################################################
		## main function/ code

if __name__ == "__main__":
	
	try:
		print("Starting server...")
		
		#create bluetooth socket
		try:
			server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
			server.bind(("",BTPortNo))
			server.listen(1)
		except:
			print("unable to create/bind scocket")
	
		while(ServerOn):
			connected = 0
			while(not connected):
				# accept connection from client
				print("Waiting for connection from client on [RFCOMM port=%d]" % BTPortNo)
				try:
					client,client_info = server.accept()
					print("Connected to",client_info)
					connected = 1
				except:
					pass

			#send/recieve to/from client
			try:
				while connected:
					RxData = client.recv(RxBuffSize)
					RxData = ast.literal_eval(RxData)
					print(RxData)

					command_dictionary[RxData[0]](RxData)

			except:
				pass

	#handle exceptions/ctrl + c
	except KeyboardInterrupt:
		print("Shutting down...")
		client.close()
		server.close()
	except:
		client.close()
		server.close()		
