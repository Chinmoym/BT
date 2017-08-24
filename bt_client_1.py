import bluetooth
#import subprocess #required for chip only
import ast

#Global variables
BTPortNo = 3
TargetAddress = None
command_list = ["['detectall']",\
		"['initialize',0x10]",\
		"['getinfo',0x10]",\
		"['readfrom',0x10,0x30]",
		"['writeto',0x10,0x30,0xff]",\
		"quit"
		]

#make the bluetooth device discoverable
#subprocess.call(['sudo','hciconfig','hci0','piscan'])

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
			#services = bluetooth.find_Service(address=target_address)
			#print(services)
			break
	if TargetAddress == None:
		print("No chip device avaialble")
	else:
		client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		client.connect((TargetAddress,BTPortNo))
		print("connected to ",TargetAddress)
		try:
			for indx in range(0,5):
				#command = raw_input()
				command  = command_list[indx]
				client.send(command)
				if command == "quit":
					print("Quit command")
					client.close()
				print(command)
		except KeyboardInterrupt:
			print("Shutting down...")
			client.close()
		except:
			client.close()
