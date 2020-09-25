#python socket
import socket
s=socket.socket() #khoit ao connect
host=socket.gethostname() #get host name
port=12347

s.connect((host,port))  #connect nhan 1 tuple()
print(s.recv(1024)) #nhan du lieu tu s qua tcp
s.close()

#cach 2
s=socket.socket() #khoit ao connect
host=socket.gethostname() #get host name
port=12347

s.bind((host,port)) #lang nghe den dia chi host va port

s.listen() #thiet lap mo ket noi tren server. tham so truyen vao la so ket noitoi da
while True():
    c,addr=s.accept() #chap nhan ket noi va tra ve 1 tuple chua connection va adrress
    print("Got connection from:",addr)
    c.send(b'Thank you for connecting') #gui du lieu qua tcp
    c.close()
s.close() # dong ket noi
