############################################################################################################
		## LIBRARIES
import bluetooth
import subprocess #required for chip only
import ast
from time import sleep
from time import time


###########################################################################################################
		## Global variables
BTPortNo = 3
TargetMACAddress = 'A0:2C:36:9D:D3:AF' 
#TargetMACAddress = '68:17:29:45:5F:32'
AddressList = ''
client = ''

######################################################################################################
######## Variables for performance Analysis
DeviceAddress = '119'
Read_RegisterAddress = '0xF6'
Write_RegisterAddress = '0xF4'
Value = '0x34'

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
	f= open("Time_analysys.txt","a+")

	diff = end - start 
	f.write("Detectall = %f9 | " %(diff))
	diff = end_send - start 
	f.write("Detectall send = %f9 | " %(diff))

	f.close()
	#e................................

	#AddressList = ast.literal_eval(AddressList)
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
	command = '[\"getinfo\",'+DeviceAddress+']'
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
	f= open("Time_analysys.txt","a+")
	diff = end - start 
	f.write("Getinfo = %f9 | " %(diff))
	diff = end_send - start 
	f.write("Getinfo Send = %f9 | " %(diff))
	f.close()
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
	command = '[\"readfrom\",'+DeviceAddress+','+Read_RegisterAddress+']'
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
	f= open("Time_analysys.txt","a+")
	diff = end - start 
	f.write("Readfrom = %f9 | " %(diff))
	diff = end_send - start 
	f.write("Readfrom Send = %f9 | " %(diff))
	f.close()
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
	command = '[\"writeto\",'+DeviceAddress+','+Write_RegisterAddress+','+Value+']'
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
	f= open("Time_analysys.txt","a+")

	diff = end - start 
	f.write("Writeto = %f9 | " %(diff))
	diff = end_send - start 
	f.write("Writeto send= %f9\n " %(diff))
	f.close()
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
				diff = end - start 
				f= open("Time_analysys.txt","a+")
				f.write("Scan= %f9 | " %(diff))
				f.close()
				#e................................
			except KeyboardInterrupt:
				exit()
			except:	
				print("unable to discover device, check your bluetooth settings")
			print(NearbyDevices)
	
			# discover and connect to chip
			for Address in NearbyDevices:
				# discover chip based on MAC address
				try:
					name = bluetooth.lookup_name(Address)
				except:
					print("unable to fetch name")
				print (name,Address,TargetMACAddress)
				if Address == TargetMACAddress:
					print("Services available with chip server",TargetMACAddress)
					#s................................
					start = time()
					#e................................

					services = bluetooth.find_service(address=TargetMACAddress)
					#s................................
					end = time()
					diff = end - start 
					f= open("Time_analysys.txt","a+")
					f.write("Service List= %f9 | " %(diff))
					f.close()
					#e................................

					print(services)
					#s.....Commented nxt 3 lines for Performance analysis
#					con = raw_input("Do you wish to connect [n for no]:")
#					if con == "n":
#						continue
					#e......Comments end

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
						diff = end - start 
						f= open("Time_analysys.txt","a+")
						f.write("Connect= %f9 | " %(diff))
						f.close()
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
							if command == "quit": # quit command to exit only client
								client.send('[\"quit\"]')
								print("closing client")
								client.close()
								connected = 0
								exit()
#							elif command not in command_list: # inavalid commands
#								print("command not in command list"+"\n")
							else: # valid commands
								try:
									command_dictionary[command]()
									sleep(1)
								except KeyboardInterrupt:
									print("Closing client")
									client.close()
								except:
									print("closing client")
									client.close()
#e............................................................
	except KeyboardInterrupt:
		print("exit")
	except:
		print("exit")
