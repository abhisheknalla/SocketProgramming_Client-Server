import socket
import os
import sys

HOST = ''
PORT = 1024
socket = socket.socket()

dir = "Data/"
print("Server running...")
socket.bind((HOST, PORT))
socket.listen(5)

while(1):
    conn, addr = socket.accept()
    print("Connected to Client IP:",addr)

    fname = conn.recv(1024)

    k = os.path.exists(dir+fname)

    if k==0:
        conn.send("1")
        continue
    else:
        conn.send("0")

    f = open(dir+fname,"rb")
    l = f.read(1024)

    while(l):
        conn.send(l)
        l = f.read(1024)

    f.close()
    print('File sent to server')
    conn.close()
