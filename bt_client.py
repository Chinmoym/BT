############################################################################################################
		## LIBRARIES
# In this section all the python library dependencies for working of the code is listed
import bluetooth						# bluetooh library from PyBluez
import subprocess 						
import ast							# for data formatting (string to literals)
from time import sleep						# for sleep/delay function


###########################################################################################################
		## Global variables
# This section contains any global variables used through out the code
BTPortNo = 3							# BT port no used valid values (1-31)
TargetMACAddress = 'A0:2C:36:9D:D3:AF'				# server MAC address
#TargetMACAddress = '68:17:29:45:5F:32'
AddressList = ''						
client = ''							# client socket


###########################################################################################################
		## Functions and utilities

#make the bluetooth device discoverable
subprocess.call(['sudo','hciconfig','hci0','piscan'])

# detectall command
# syntax : detectall
# usage  : the user sends the string "detectall" from terminal once the code is up, if all valid, a resopose
# 		with list of I2C device address will be recieved.
def detectall():
	command = '[\"detectall\",\"\"]'
	client.send(command)
	try:
		AddressList = client.recv(1024)
	except:
		print("error recieving")	
	#AddressList = ast.literal_eval(AddressList)
	print(AddressList)	

# getinfo command
# syntax : getinfo [device address]
# usage  : the user first sends "getinfo" from terminal, then another prompt asking for the I2C device
#		address is given, provide the device address in hex/decimal, an appropriate list of all
# 		registers of the device is recieved from server
def getinfo():
	DeviceAddress = raw_input("Enter device address for device info:")
	command = '[\"getinfo\",'+DeviceAddress+']'
	client.send(command)
	DeviceInfo = client.recv(1024)
	#DeviceInfo = ast.literal_eval(DeviceInfo)
	print(DeviceInfo)

# readform command
# syntax : readfrom [device address] [register address]
# usage  : the user first send "readfrom" from terminal, then the user is prompted with two successive 
#		prompts asking for 'I2C device address' and 'register address' from where you want to read.
#		On success the register value is recieved.
def readfrom():
	DeviceAddress = raw_input("Enter device address:")
	RegisterAddress = raw_input("Enter register address:")
	command = '[\"readfrom\",'+DeviceAddress+','+RegisterAddress+']'
	client.send(command)
	RegisterValue = client.recv(1024)
	print(RegisterValue)

# writeto command
# syntax: writeto [device address][register address][Value]
# usage  : the user first send "writeto" from terminal, then the user is prompted with three successive 
#		prompts asking for 'I2C device address', 'register address' and 'the value' to be wriiten.
#		On success a write succesful ack is provided.
def writeto():
	DeviceAddress = raw_input("Enter device address:")
	RegisterAddress = raw_input("Enter register address:")
	Value = raw_input("Enter value to be written:")
	command = '[\"writeto\",'+DeviceAddress+','+RegisterAddress+','+Value+']'
	client.send(command)
	WriteAck = client.recv(1024)
	print(WriteAck)


##########################################################################################################
		## command dictionary to lookup
# this is a dictionary in python which allows us to do a mapping between two values, here we use it to 
# decode the fucntion from the string recieved from user terminal
command_dictionary = {   "detectall" 	: detectall, \
#			"initialize" 	: initialize, \
			"getinfo"	: getinfo, \
			"readfrom"	: readfrom, \
			"writeto"	: writeto \
		    }



###########################################################################################################
		## main function/code
# write your core functioanlity here
	
if __name__ == "__main__":
	
	try:
		while(1):
			# search for nearby BT devices
			print("Searching for nearby devices...")
			try:
				NearbyDevices = bluetooth.discover_devices()
			except KeyboardInterrupt:
				exit()
			except:
				print("unable to discover device, check your bluetooth settings")
			print(NearbyDevices)
	
			
			# scan through all the available BT devices and if the server MAC is found
			# then connect to the server
			for Address in NearbyDevices:
				# this step is just to get the name of the BT device, it is not used
				# anywhere just for information purpose
				try:
					name = bluetooth.lookup_name(Address)
				except:
					print("unable to fetch name")
				print (name,Address,TargetMACAddress)
				# connect to the server if MAC address is found
				if Address == TargetMACAddress:
					# search for the service broadcasted by server
					print("Services available with chip server",TargetMACAddress)
					services = bluetooth.find_service(address=TargetMACAddress)
					for ser in services:
						if ser['name'] == "Chip device":
							print ser  # this display only the service with serial_port
									# the service addtion we did
									# check the description portion for the device
									# address
				
					#con = raw_input("Do you wish to connect [n for no]:")
					#if con == "n":
					#	continue

					# connect to a chip server and create a client socket 
					print("connecting to chip server",TargetMACAddress)
					try:
						client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
						client.connect((TargetMACAddress,BTPortNo))
						print("connected to ",TargetMACAddress)
						connected = 1
					except:
						print("error connecting to device")
						continue

					# once successfully connected provide the user with intearctive facility in
					# the terminal to send commands to server, refer each command function area
					# for the syntax of each commands
					while(connected):
						print("Enter command")
						print("Supported commands: [detectall][getinfo][readfrom][writeto][quit]")
						command = raw_input(">")
						if command == "quit": # quit command to exit
							client.send('[\"quit\"]')
							print("closing client")
							client.close()
							connected = 0
							exit()
						#elif command not in command_list: # inavalid commands
						#	print("command not in command list"+"\n")
						else: # valid commands
							try:
								command_dictionary[command]()
								sleep(1)
							except KeyboardInterrupt:
								print("Closing client")
								client.close()
								exit()
							except:
								print("closing client")
								client.close()
								exit()
	except KeyboardInterrupt:
		print("ctrl^C forced exit")
		exit()
	except:
		print("exit")
		exit()
