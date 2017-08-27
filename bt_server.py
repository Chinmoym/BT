#inlcude library dependencies
import bluetooth
import subprocess
import ast
import sensor_top

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
			#end the connection from master
			if RxData=="quit":
				print("Master disconnected")
				client.close()
				#wait for another connection
				print("Waiting for connection from master [RFCOMM port=%d]" % BTPortNo)
				client,client_info = server.accept()
				print("Connected to",client_info)
			
			Rx = ast.literal_eval(RxData)

			if Rx[0]=="detectall":
				data = sensor_top.detectall()
				data_send = '[\"' + data +'\"]'
				client.send(data_send)

			elif Rx[0]=="getinfo":
				print(Rx[1])
				info = sensor_top.getinfo(Rx[1])
				client.send(info)

			elif Rx[0]=="readfrom":
				data = sensor_top.read_from(Rx[1],Rx[2])
				data = format(data, '#04X')
				ret1 = Rx[1]
				ret2 = str(format(Rx[2], '#04X'))
				data_send = '[\"' + ret1 + '\",\"' + ret2 +'\", \"' + str(data) + '\"]'
				client.send(data_send)

			elif Rx[0]=="writeto":
				sensor_top.write_to(Rx[1],Rx[2],Rx[3])
				client.send("Write OK")

			elif Rx[0]=="initialize":
				sensor_top.initialize(Rx[1])
				data_send =  Rx[1] + ' is initialized' 
				client.send(data_send)

			elif Rx[0]=="Get_Temp":
				data = sensor_top.get_temperature()
				data_send = '[\"' + str(data) + '\"]'
				client.send(data_send)

			elif Rx[0]=="Get_Pressure":
                                data = sensor_top.get_pressure()
                                data_send = '[\"' + str(data) + '\"]'
				print(data_send)           
                                client.send(data_send)
				
			else:
				client.send("Wrong Input")
				print("Wrong input received")
				

	#handle exceptions/ctrl + c
	except KeyboardInterrupt:
		print("Shutting down...")
		client.close()
		server.close()
	except:
		client.close()
		server.close()		
		
	

