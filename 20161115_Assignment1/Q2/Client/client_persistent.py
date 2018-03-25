import socket
host=""
port =5678

s=socket.socket()
fil=raw_input("Enter the filename(s): ")
s.connect((host,port))
size=len(fil)
size = bin(size)[2:].zfill(16)
s.send(size)
s.send(fil)

while True:
    a=s.recv(16)
    if not a:
        break
    a=int(a,2)
    size=s.recv(16)
    size=int(size,2)
    filename=s.recv(size)
    if a is not 1:
        print filename + ' doesnt exist'

    else:
        fsize=s.recv(32)
        fsize=int(fsize,2)
        flg = 0
        File=open(filename,'wb')
        xsiz=4096
        while fsize > 0:
            if fsize < xsiz:
                xsiz=fsize
            data=s.recv(xsiz)
            File.write(data)
            fsize-=len(data)
        File.close()


s.close()
