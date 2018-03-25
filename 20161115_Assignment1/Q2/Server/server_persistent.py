import socket,os

host=""
port=5678

#dir = "/Data/"
def send(s,file):
    size=len(file)
    size=bin(size)[2:].zfill(16)
    s.send(size)
    s.send(file)
    file = "Data/" + file
    fize=os.path.getsize(file)
    fize=bin(fize)[2:].zfill(32)
    s.send(fize)
    File=open(file,'rb')
    l=File.read()
    s.sendall(l)
    File.close()

s = socket.socket()
s.bind((host,port))
s.listen(5)

while True:
    conn,addr = s.accept()
    print 'Server Started'
    flg=1
    size= conn.recv(16)
    size=int(size,2)
    data=conn.recv(size)
    fnames=data.split()

    for f in fnames:
        filepath = "Data/" + f
        if os.path.isfile(filepath):
            key=1
            key=bin(key)[2:].zfill(16)
            conn.send(key)
            file=f
            send(conn,file)
        else:
            key=0
            key=bin(key)[2:].zfill(16)
            conn.send(key)
            size=len(f)
            flg=0
            size = bin(size)[2:].zfill(16)
            conn.send(size)
            conn.send(f)
            print f + " does not exist"
    conn.close()
