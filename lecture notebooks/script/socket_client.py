import socket

HOST = socket.gethostname()    
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.sendall(b'Hello, world')

data = sock.recv(1024)

sock.close()

print('Received', repr(data))
