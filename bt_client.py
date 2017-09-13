import bluetooth
import subprocess #required for chip only
import ast

from time import sleep

#Global variables
BTPortNo = 3
TargetAddress = None
#dummy command list to test
command_list = ['[\"detectall\"]',\
		'[\"initialize\",\"BMP085\"]',\
		'[\"getinfo\",\"BMP085\"]',\
		'[\"readfrom\",\"BMP085\",0xF4]',\
		'[\"writeto\",\"BMP085\",0xF4,0x34]',\
		'[\"readfrom\",\"BMP085\",0xF4]',\
		'[\"Get_Temp\"]',\
		'[\"Get_Pressure\"]',\
		"quit"\
		]


#make the bluetooth device discoverable
subprocess.call(['sudo','hciconfig','hci0','piscan'])

#main function/code
if __name__ == "__main__":
	#serach for devices
	print("Searching for nearby devices...")
	NearbyDevices = bluetooth.discover_devices()
	print(NearbyDevices)
	#connect to chip
	for device in NearbyDevices:
		name = bluetooth.lookup_name(device)
		print (name,device)
		if name=="chip":
			print("Connecting to chip")
			TargetAddress = device
			services = bluetooth.find_service(address=TargetAddress)
			print(services)
			break
	if TargetAddress == None:
		print("No chip device avaialble")
	else:
		client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		client.connect((TargetAddress,BTPortNo))
		print("connected to ",TargetAddress)
		print ""
		try:
			for command in command_list	:
				#command = raw_input()

				if command == "quit":
					print("Quit command")
					client.close()
				client.send(command)

				print command


				if command == command_list[0]:				#detectall
					add_list = client.recv(1024)
					add_list = ast.literal_eval(add_list)
					for add in add_list:
						print add
					print ""


				elif command == command_list[1]:			#initialize
					Ack_packet = client.recv(1024)
					print Ack_packet
					print ""

				elif command == command_list[2]:			#getinfo
					Dev_info = client.recv(1024)
					print  "Device name is " + ast.literal_eval(Dev_info)[0]
					Dev_info = ast.literal_eval(ast.literal_eval(Dev_info)[1])
					print "Available Registers and commands are:" 
					print Dev_info[0]
					print Dev_info[1]
					print Dev_info[2]
					print Dev_info[3]
					print Dev_info[4]
					print ""

				elif command == command_list[3]:			#readfrom
					Register = client.recv(1024)
					#print Register
					print "Value of Register " + ast.literal_eval(Register)[1] + " Of Device at add " + ast.literal_eval(Register)[0] +" is " + ast.literal_eval(Register)[2]
					print ""

				elif command == command_list[4]:			#writeto
					print client.recv(1024)
					print ""

				elif command == command_list[5]:			#readfrom
					Register = client.recv(1024)
					print "Value of Register " + ast.literal_eval(Register)[1] + " Of Device at add " + ast.literal_eval(Register)[0] +" is " + ast.literal_eval(Register)[2]
					print ""	

				elif command == command_list[6]:			#get temperature
					print "Temperature is " + ast.literal_eval(client.recv(1024))[0] + " degree celcius"
					print ""
				
				elif command == command_list[7]:			#get pressure
					print "Pressure is " + ast.literal_eval(client.recv(1024))[0] + "Pa"
					print ""




				sleep(1)
		except KeyboardInterrupt:
			print("Shutting down...")
			client.close()
		except:
			client.close()
