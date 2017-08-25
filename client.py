# client file

import socket

s = socket.socket()
host = socket.gethostname()
port = 65534

s.connect((host, port))
print(str(s.recv(1024)))
s.close()
