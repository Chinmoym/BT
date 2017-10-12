#############################################################################################################
		## library dependencies
import bluetooth
import subprocess
import ast
import sensor_top
import thread

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

""" 	x	: received command
    	client	: client from which <x> is sent
	*Sends the the result as a string to the <client>*
"""
def detectall(x,client): # detectall command
	data = sensor_top.detectall()
	TxData = '[\"'+str(data)+'\"]'
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass
	
def getinfo(x,client): # getinfo command
	data = sensor_top.getinfo(x[1])
	TxData = '[\"'+data+'\"]'
	try:
		client.send(TxData)
	except:
		print("error sending reply")
		pass

def readfrom(x,client):
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

def writeto(x,client):
	data = sensor_top.writeto(x[1],x[2],x[3])
	TxData = '[\"data\"]'
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

#create new thread for each client
def new_client(threadname,delay,client,client_info):
        try:
                print(client,client_info)
                while True:
                        RxData = client.recv(1024)
                        RxData = ast.literal_eval(RxData)
                        print(client_info,"Recieved command:",RxData)
                        command_dictionary[RxData[0]](RxData,client)
        except:
                pass


###########################################################################################################
		## main function/ code

if __name__ == "__main__":

	print("Starting server...")
	#create bluetooth socket and acept connection from master
	server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	server.bind(("",BTPortNo))
	server.listen(1)

	strin = "Chip device"
	myinfo = sensor_top.detectall()
	
	bluetooth.advertise_service(server,strin,service_classes = [bluetooth.SERIAL_PORT_CLASS],\
					profiles=[bluetooth.SERIAL_PORT_PROFILE]\
					, description = str(myinfo))
	try:
		print("Waiting for connection from master [RFCOMM port=%d]" % BTPortNo)
		while(1):
			try:
				client,client_info = server.accept()
				print("Connected to",client_info)
				thread_name = '_'+client_info[0]
				thread.start_new_thread(new_client,(thread_name,0,client,client_info))
							
			#handle exceptions/ctrl + c
			except KeyboardInterrupt:
				print("Shutting down...")
				client.close()
				server.close()
			except:
				pass
				#client.close()
	except KeyboardInterrupt:
		print("Shuttig down...")
		client.close()
		server.close()		
	except:
		print("exit")
		client.close()
		server.close()
