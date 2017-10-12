############################################################################################################
		## LIBRARIES
import bluetooth
import subprocess #required for chip only
import ast
from time import sleep
from time import time
import random 


###########################################################################################################
		## Global variables
BTPortNo = 3
TargetMACAddress = 'A0:2C:36:9D:D3:AF' 
#TargetMACAddress = '68:17:29:45:5F:32'
AddressList = ''
client = ''
AL = ''


flag=0
DA =0
DAS = 0
GI=0
GIS=0
RF=0
RFS=0
WT=0
WTS=0
SCAN=0
SER=0
CON=0
######################################################################################################
######## Variables for performance Analysis
DeviceAddress = ['0x77','0x53']
Read_RegisterAddress = '0xF6'
Write_RegisterAddress = '0xF4'
Value = '0x34'
dev_addr = random.choice(DeviceAddress)

###########################################################################################################
		## Command List Performance analysis
command_list = ['detectall',\
		'getinfo',\
		'readfrom',\
		'writeto',\
		'quit'\
		]


###########################################################################################################
		## Functions and utilities

#make the bluetooth device discoverable
subprocess.call(['sudo','hciconfig','hci0','piscan'])

# detectall command
# sysntax : detectall
def detectall():
	command = '[\"detectall\",\"\"]'
	#s................................
	start = time()
	#e................................
	client.send(command)			
	#s................................
	end_send = time()
	#e................................
	
	try:
		AddressList = client.recv(1024)
	except:
		print("error recieving")	
	#s................................
	end = time()
	global DA
	DA = end - start
	global DAS 
	DAS = end_send - start 
	#e................................

	print(AddressList)	

# initialize command
# syntax : initialize [address]
'''def initialize():
	DeviceAddress = raw_input("Enter address of device to initialize:")
	command = '["initialize",'+DeviceAddress+']'##################################################################################
	client.send(command)
	Ack = client.recv(1024)
	print Ack
'''
# getinfo command
# syntax : getinfo [device address]
def getinfo():
#s...comented for performance measurement
#	DeviceAddress = raw_input("Enter device address for device info:")
#e...comment end
	
	command = '[\"getinfo\",'+dev_addr+']'
	#s................................
	start = time()
	#e................................
	client.send(command)
	#s................................
	end_send = time()
	#e................................

	DeviceInfo = client.recv(1024)
	#s................................
	end = time()
	global GI
	GI = end - start
	global GIS 
	GIS = end_send - start 
	#e................................

	#DeviceInfo = ast.literal_eval(DeviceInfo)
	print(DeviceInfo)

# readform command
# syntax : readfrom [device address] [register address]
def readfrom():
#s...comented for performance measurement
#	DeviceAddress = raw_input("Enter device address:")
#	Read_RegisterAddress = raw_input("Enter register address:")
#e...comment end
	if dev_addr == '0x77':
		Read_RegisterAddress = '0xF6'
	else:
		Read_RegisterAddress = '0x1F'
	command = '[\"readfrom\",'+dev_addr+','+Read_RegisterAddress+']'
	#s................................
	start = time()
	#e................................

	client.send(command)

	#s................................
	end_send = time()
	#e................................

	RegisterValue = client.recv(1024)

	#s................................
	end = time()
	global RF
	RF = end - start
	global RFS 
	RFS = end_send - start 
	#e................................
	print(RegisterValue)

# writeto command
# syntax: writeto [device address][register address][Value]
def writeto():
#s...comented for performance measurement
#	DeviceAddress = raw_input("Enter device address:")
#	Write_RegisterAddress = raw_input("Enter register address:")
#	Value = raw_input("Enter value to be written:")
#e...comment end
	
	if dev_addr == '0x77':
		Write_RegisterAddress = '0xF4'
		value = '0x34'
	else:
		Write_RegisterAddress = '0x1F'
		value = '0x01'
	command = '[\"writeto\",'+dev_addr+','+Write_RegisterAddress+','+Value+']'
	#s................................
	start = time()
	#e................................
	client.send(command)
	#s................................
	end_send = time()
	#e................................
	WriteAck = client.recv(1024)
	#s................................
	end = time()
	global WT
	WT = end - start
	global WTS
	WTS = end_send - start 
	#e................................
	print(WriteAck)


##########################################################################################################
		## command dictionary to lookup
command_dictionary = {   "detectall" 	: detectall, \
#			"initialize" 	: initialize, \
			"getinfo"	: getinfo, \
			"readfrom"	: readfrom, \
			"writeto"	: writeto \
		    }



###########################################################################################################
		## main function/code

if __name__ == "__main__":
	
	try:
		
		while(1):
			# search for BT devices
			print("Searching for nearby devices...")
			try:
				#s................................
				start = time()
				#e................................

				NearbyDevices = bluetooth.discover_devices()
				
				#s................................
				end = time()
				SCAN = end - start 
				#e................................
			except KeyboardInterrupt:
				exit()
			except:	
				print("unable to discover device, check your bluetooth settings")
				f= open("cli_70:77:81:99:D1:7C.txt","a+")
				f.write("-1|%f|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1\n " %(SCAN))
				f.close()

			print(NearbyDevices)
	
			# discover and connect to chip
			for Address in NearbyDevices:
				# discover chip based on MAC address
				try:
					name = bluetooth.lookup_name(Address)
				except:
					print("unable to fetch name")
					f= open("cli_70:77:81:99:D1:7C.txt","a+")
					f.write("%f|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1\n " %(SCAN))
					f.close()

				print (name,Address,TargetMACAddress)
				if Address == TargetMACAddress:
					flag = 1
					print("Services available with chip server",TargetMACAddress)
					#s................................
					start = time()
					#e................................

					services = bluetooth.find_service(address=TargetMACAddress)
					#s................................
					end = time()
					SER = end - start 
					#e................................

					print(services)

					# connect to a chip server 
					print("connecting to chip server",TargetMACAddress)
					try:
						#s................................
						start = time()
						#e................................

						client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
						client.connect((TargetMACAddress,BTPortNo))
						#s................................
						end = time()
						CON = end - start 
						#e................................

						print("connected to ",TargetMACAddress)
						connected = 1
					except:
						print("error connecting to device")

						continue

					# send commands to server
					while(connected):
						print("Enter command")
						print("Supported commands: [detectall][getinfo][readfrom][writeto][quit]")
#Comment Start for performance
#						command = raw_input(">")
#Comment end for performance
#s.............................................................
						for command in command_list:
#added Indent till else ends
							if command != 'quit': # valid commands
								try:
									command_dictionary[command]()
									sleep(1)
								except KeyboardInterrupt:
									print("Closing client")
									client.close()
								except:
									print("closing client")
									client.close()
							if command == 'quit': # quit command to exit only client
								client.send('[\"quit\"]')
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%s|" %(dev_addr))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(SCAN))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(SER))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(CON))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(DA))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(GI))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(RF))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(WT))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(DAS))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(GIS))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f|" %(RFS))
								f = open("cli_70:77:81:99:D1:7C.txt","a+")
								f.write("%f\n" %(WTS))
								#f.write("%f | %f | %f | %f | %f | %f | %f | %f | %f | %f | %f | %f\n" %(DeviceAddress) %(SCAN) %(SER) %(CON) %(DA) %(GI) %(RF) %(WT) %(DAS) %(GIS) %(RFS) %(WTS))
								f.close()

								print("closing client")
								client.close()
								connected = 0

								exit()
#							elif command not in command_list: # inavalid commands
#								print("command not in command list"+"\n")
			if flag ==0:
				f= open("cli_70:77:81:99:D1:7C.txt","a+")
				f.write("-1|%f|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1\n" %(SCAN))
				f.close()

						

#e............................................................
	except KeyboardInterrupt:
		print("exit")
		exit()
	except:
		print("exit")
		print "exit"
		exit()
