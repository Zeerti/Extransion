import socket
import time
import pickle



HEADERSIZE = 10


# AF_INET = IPV4, SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 1234))
print(f'\nListening at {socket.gethostname()} on port 1234...')
# size of queue
s.listen(40)

while True:
    #Remote socket object, IP of connected computer
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established')

    d = {1:"Hey", 2:"There"}
    msg = pickle.dumps(d)
    

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(msg)
