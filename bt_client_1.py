import bluetooth
import ast

port = 3

print("Searching for nearby devices...")
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
                #print(services)
                break

client = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
client.connect((target_address, port))


print("connected.")
try:
        while True:
                RxData = ast.literal_eval(client.recv(1024))
                print("Name = [%s]" % RxData[0])
                #connect_to_i2c(RxData[0],RxData[1],RxData[2])
                client.send("OK")
except:
        client.close()
