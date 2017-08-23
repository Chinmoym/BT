
import bluetooth
import subprocess


subprocess.call(['sudo','hciconfig','hci0','piscan'])

port = 3
server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server.bind(("",port))
server.listen(1)
#port = server.getsockname()[1]  

#UUID = "00001800-0000-1000-8000-00805f9b34fb"
UUID = "Generic Access Profile"

#print("advertise my class")
#bluetooth.advertise_service(server,"CHIP",service_id=UUID, \
#service_classes = [(UUID,SERIAL_PORT_CLASS)],profiles=[SERIAL_PORT_PROFILE])


print("Waiting for connection on RFCOMM port %d" % port)
client, client_info = server.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client.recv(1024)
        if data == "quit": 
		break
        print("received [%s]" % data)
except: 
	print("disconnected")
	client.close()
	server.close()
