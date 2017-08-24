#inlcude library dependencies
import bluetooth
import subprocess
import ast

#Global variables
RxBuffSize = 4096
BTPortNo = 3

#make the bluetooth device discoverable
subprocess.call(['sudo','hciconfig','hci0','piscan'])


#main function/ code
if __name__ == "__main__":
	print("Starting server...")
	#create bluetooth socket and acept connection from master
	server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	server.bind(("",BTPortNo))
	server.listen(1)
	print("Waiting for connection from master [RFCOMM port=%d]" % BTPortNo)
	client,client_info = server.accept()
	print("Connected to",client_info)
	#send/recieve to/from master
	try:
		while True:
			RxData = client.recv(RxBuffSize)
			print(RxData)
			Rx = ast.literal_eval(RxData)
			print(Rx)
			#end the connection from master
			if RxData=="quit":
				print("Master disconnected")
				client.close()
				#wait for another connection
				print("Waiting for connection from master [RFCOMM port=%d]" % BTPortNo)
				client,client_info = server.accept()
				print("Connected to",client_info)
	#handle exceptions/ctrl + c
	except KeyboardInterrupt:
		print("Shutting down...")
		client.close()
		server.close()
	except:
		client.close()
		server.close()		
		
	
