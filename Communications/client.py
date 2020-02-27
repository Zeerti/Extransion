import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 50000))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print(f'Received: {data}')