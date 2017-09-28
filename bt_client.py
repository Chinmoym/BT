############################################################################################################
		## LIBRARIES
import bluetooth
import subprocess #required for chip only
import ast
from time import sleep



###########################################################################################################
		## Global variables
BTPortNo = 3
#TargetMACAddress = 'A0:2C:36:9D:D3:AF' 
TargetMACAddress = '68:17:29:45:5F:32'
AddressList = ''
client = ''


###########################################################################################################
		## Functions and utilities

#make the bluetooth device discoverable
subprocess.call(['sudo','hciconfig','hci0','piscan'])

# detectall command
# sysntax : detectall
def detectall():
	command = '[\"detectall\",\"\"]'
	client.send(command)
	try:
		AddressList = client.recv(1024)
	except:
		print("error recieving")	
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
	DeviceAddress = raw_input("Enter device address for device info:")
	command = '[\"getinfo\",\"'+DeviceAddress+'\"]'
	client.send(command)
	DeviceInfo = client.recv(1024)
	#DeviceInfo = ast.literal_eval(DeviceInfo)
	print(DeviceInfo)

# readform command
# syntax : readfrom [device address] [register address]
def readfrom():
	DeviceAddress = raw_input("Enter device address:")
	RegisterAddress = raw_input("Enter register address:")
	command = '[\"readfrom\",\"'+DeviceAddress+'\",\"'+RegisterAddress+'\"]'
	client.send(command)
	RegisterValue = client.recv(1024)
	print(RegisterValue)

# writeto command
# syntax: writeto [device address][register address][Value]
def writeto():
	DeviceAddress = raw_input("Enter device address:")
	RegisterAddress = raw_input("Enter register address:")
	Value = raw_input("Enter value to be written:")
	command = '[\"writeto\",\"'+DeviceAddress+'\",\"'+RegisterAddress+'\",\"'+Value+'\"]'
	client.send(command)
	WriteAck = client.recv(1024)
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
				NearbyDevices = bluetooth.discover_devices()
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
					services = bluetooth.find_service(address=TargetMACAddress)
					print(services)
					print('')
					con = raw_input("Do you wish to connect [n for no]:")
					if con == "n":
						continue

					# connect to a chip server 
					print("connecting to chip server",TargetMACAddress)
					try:
						client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
						client.connect((TargetMACAddress,BTPortNo))
						print("connected to ",TargetMACAddress)
						connected = 1
					except:
						print("error connecting to device")
						continue

					# send commands to server
					while(connected):
						print("Enter command")
						print("Supported commands: [detectall][getinfo][readfrom][writeto][quit]")
						command = raw_input(">")
						if command == "quit": # quit command to exit only client
							client.send('[\"quit\"]')
							print("closing client")
							client.close()
							connected = 0
							exit()
#						elif command not in command_list: # inavalid commands
#							print("command not in command list"+"\n")
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
	except KeyboardInterrupt:
		print("exit")
	except:
		print("exit")
