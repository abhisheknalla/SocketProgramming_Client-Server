Roll Number1 : 20161115
Roll Number2 : 20161191

Q1 written in C and Q2 in python2

Q1 Compile:
gcc server.c -o server -pthread
gcc client.c -o client -pthread

File names available in Data: a.txt b.txt c.txt

Q1 Run:
./server
./client (after it ask for filling IP(127.0.0.1) and filename)


-----------------------------------------------------------------------


Run Q2:

Persistent:

python2 server_persistent.py
python2 client_persistent.py

Non-persistent:
python2 server_nonpersistent.py
python2 client_nonpersistent.py

File names available in Data: file1.txt file2.txt file3.txt


The persistent connection should run faster than non-persistent connection. 
