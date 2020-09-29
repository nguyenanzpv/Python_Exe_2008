import socket
s=socket.socket()
host=socket.gethostname()
port=12347
s.bind(host,port)

s.listen()
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send(b'Thank you for connection')
    c.close()
s.close()
    