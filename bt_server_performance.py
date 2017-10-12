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

DA =0
DAS = 0
I2CDA=0
GI=0
GIS=0
I2CGI=0
RF=0
RFS=0
I2CRF=0
WT=0
WTS=0
I2CWT=0

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
        global DA
        DA = end - start
        global I2CDA
        I2CDA = end_I2c - start
        global DAS
        DAS = end_send - start_send
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
        global GI
        GI = end - start
        global I2CGI
        I2CGI = end_I2c - start
        global GIS
        GIS = end_send - start_send
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
        global RF
        RF = end - start
        global I2CRF
        I2CRF = end_I2c - start
        global RFS
        RFS = end_send - start_send
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
        global WT
        WT = end - start
        global I2CWT
        I2CWT = end_I2c - start
        global WTS
        WTS = end_send - start_send
        #e................................

def quit__():
	print "quit"        
	


###########################################################################################################
		## command dictionary to lookup
command_dictionary = {	"detectall"	: detectall, \
			#"initialize"	: initialize, \
			"getinfo"	: getinfo, \
			"readfrom"	: readfrom, \
			"writeto"	: writeto, \
			"quit"		: quit__\
			}

###########################################################################################################

#create new thread for each client
def new_client(threadname,delay,client,client_info):
        try:
                print(client,client_info)
                filename = "ser_" + client_info[0] + ".txt"
                while True:
                        RxData = client.recv(1024)
                        RxData = ast.literal_eval(RxData)
                        print(client_info,"Recieved command:",RxData)
                        if RxData[0] == "quit":
                                f = open(filename,"a+")
                                f.write("%f|" %(DA))
                                f = open(filename,"a+")
                                f.write("%f|" %(GI))
                                f = open(filename,"a+")
                                f.write("%f|" %(RF))
                                f = open(filename,"a+")
                                f.write("%f|" %(WT))
                                f = open(filename,"a+")
                                f.write("%f|" %(I2CDA))
                                f = open(filename,"a+")
                                f.write("%f|" %(I2CGI))
                                f = open(filename,"a+")
                                f.write("%f|" %(I2CRF))
                                f = open(filename,"a+")
                                f.write("%f|" %(I2CWT))
                                f = open(filename,"a+")
                                f.write("%f|" %(DAS))
                                f = open(filename,"a+")
                                f.write("%f|" %(GIS))
                                f = open(filename,"a+")
                                f.write("%f|" %(RFS))
                                f = open(filename,"a+")
                                f.write("%f\n" %(WTS))
                                f.close()
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






