# a server file

import socket

s = socket.socket()
host = socket.gethostname()
port = 65534
s.bind((host, port))

s.listen(5)

while 1:
    c, addr = s.accept()
    print('got connection from', addr)
    c.send(b'a message that was received')
    c.close()
