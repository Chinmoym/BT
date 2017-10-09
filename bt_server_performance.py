#############################################################################################################
		## library dependencies
import bluetooth
import subprocess
import ast
import sensor_top
import thread
from time import time

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

def detectall(x,client): # detectall command
        #s................................
        start = time()
        #e................................
        data = sensor_top.detectall()
        #s................................
        end_I2c = time()
        #e................................
        print(data)
        TxData = '[\"'+str(data)+'\"]'

        print(TxData)
        try:
                #s................................
                start_send = time()
                #e................................
        
                client.send(TxData)
        
                #s................................
                end_send = time()
                #e................................
        except:
                print("error sending reply")
                pass
        #s................................
        end = time()
        f= open("Time_analysys.txt","a+")
        diff = end - start
        f.write("Detectall = %f9 | " %(diff))
        diff = end_I2c - start
        f.write("I2c Detectall = %f9 | " %(diff))
        diff = end_send - start_send
        f.write("Send Responce Detectall = %f9 | " %(diff))
        
        f.close()
        #e................................

def getinfo(x,client): # getinfo command
        #s................................
        start = time()
        #e................................
        data = sensor_top.getinfo(x[1])
        #s................................
        end_I2c = time()
        #e................................

        TxData = '[\"'+data+'\"]'
        try:
                #s................................
                start_send = time()
                #e................................
        
                client.send(TxData)
        
                #s................................
                end_send = time()
                #e................................
        except:
                print("error sending reply")
                pass
        #s................................
        end = time()
        f= open("Time_analysys.txt","a+")
        diff = end - start
        f.write("Getinfo = %f9 | " %(diff))
        diff = end_I2c - start
        f.write("I2c Getinfo = %f9 | " %(diff))
        diff = end_send - start_send
        f.write("Send Responce Getinfo = %f9 | " %(diff))
        
        f.close()
        #e................................

def readfrom(x,client):
        print("readfrom::",x,x[1],x[2])
        #s................................
        start = time()
        #e................................
        data = sensor_top.readfrom(x[1],x[2])
        #s................................
        end_I2c = time()
        #e................................
        print(data)
        TxData = '[\"'+str(data)+'\"]'
        print(TxData)
        try:
                #s................................
                start_send = time()
                #e................................
        
                client.send(TxData)
        
                #s................................
                end_send = time()
                #e................................
        except:
                print("error sending reply")
                pass
        #s................................
        end = time()
        f= open("Time_analysys.txt","a+")
        diff = end - start
        f.write("Readfrom = %f9 | " %(diff))
        diff = end_I2c - start
        f.write("I2c Readfrom = %f9 | " %(diff))
        diff = end_send - start_send
        f.write("Send Responce Readfrom = %f9 | " %(diff))
        
        f.close()
        #e................................




def writeto(x,client):
        #s................................
        start = time()
        #e................................
        sensor_top.writeto(x[1],x[2],x[3])
        #s................................
        end_I2c = time()
        #e................................

        TxData = '[\"write successfull\"]'
        try:
                #s................................
                start_send = time()
                #e................................
        
                client.send(TxData)
        
                #s................................
                end_send = time()
                #e................................
        except:
                print("error sending reply")
                pass
        #s................................
        end = time()
        f= open("Time_analysys.txt","a+")
        diff = end - start
        f.write("Writeto = %f9 | " %(diff))
        diff = end_I2c - start
        f.write("I2c Writeto = %f9 | " %(diff))
        diff = end_send - start_send
        f.write("Send Responce Writeto = %f9\n" %(diff))
        
        f.close()
        #e................................

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
