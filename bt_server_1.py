import bluetooth
import subprocess

#som eglobal variables
subprocess.call(['sudo','hciconfig','hci0','piscan'])
RxBuffSize = 1024
port = 3
command = "['DEVICE_NAME','READ/WRITE','VALUE']"


if __name__ == "__main__":
        print("Starting Server...")
        server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server.bind(("",port))
        server.listen(1)
        print("Waiting connection on RFCOMM port %d" % port)
        client,client_info = server.accept()
        print("Connection to",client_info)

        try:
                while True:
                        #command = raw_input()
                        client.send(command)
                        RxData = client.recv(RxBuffSize)
                        if RxData == "quit":
                                print("Connection ended from client")
                                break
                        print("Recieved [%s]"%RxData)
        except:
                client.close()
                server.close()
