import socket
import os
import sys

HOST = ''
PORT = 1024
downloadDir = ""
filenames = raw_input('Enter the filename(s): ')
filenames = filenames.split()
for filename in filenames:
    socket1 = socket.socket()
    socket1.connect((HOST, PORT))
#    filename = sys.argv[i]
    socket1.send(filename)

    rec = socket1.recv(10)
    if rec == "1":
        print("File not found")
    else:
        with open(filename, 'wb') as file:
            while(1):
                print("Receiving data...")
                data  = socket1.recv(1024)
                if not data:
                    break
                file.write(data)
        file.close()
        print("Received file")
    socket1.close()
print("Connection Closed")
