import socket

HOST = ''        # Symbolic name meaning all available interfaces
PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

print('Connected by', addr)

while True:
    data = conn.recv(1024)
    #if not data: break
    if data:
        conn.sendall(data + b' from server!')

conn.close()
