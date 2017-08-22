
import bluetooth

port = 3

NearbyDevices = bluetooth.discover_devices()
print(NearbyDevices)

for device in NearbyDevices:
	name = bluetooth.lookup_name(device)
	addr = device
	print(name,device)
	if name=="chip":
		print("connecting to chip")
		target_address = addr
		services = bluetooth.find_service(address=target_address)
		print(services)
		break

client = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
client.connect((target_address, port))


print("connected.  type stuff")
try:
	while True:
		data = raw_input()
		if data  == "quit": 
			break
		client.send(data)
except:
	client.close()
