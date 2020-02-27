import select, socket, sys, queue
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind((socket.gethostname(), PORT))
server.listen(5)
print(f"Awaiting connections on {socket.gethostname()} from port: {PORT} ")
inputs = [server]
outputs = []
message_queues = {}

####
#### When there is the server socket in inputs, it means that a new client has arrived.
####
while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # s is a socket object
    for s in readable:
        if s is server:
            # accept incoming connection and store socket and address
            connection, client_address = s.accept()
            connection.setblocking(0)
            # Add new socket(connection) to the inputs array
            inputs.append(connection)
            #Create a new queue as a dictionary
            message_queues[connection] = queue.Queue()
        else:
            # receive sent data
            data = s.recv(1024)
            if data:
                # store the new data in the queue dictionary with a key of SOCKET type
                message_queues[s].put(data)
                # If the socket is not in OUTPUTS array
                if s not in outputs:
                    # Add socket to outputs
                    outputs.append(s)
                else:
                    # if the socket is in the outputs array...
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    # close socket connection
                    s.close()
                    print(f'Closing connection with {s}')
                    # delete socket from queue
                    del message_queues[s]
    ####                    
    #### For writable sockets, it gets pending messages (if any) and writes them to the socket. If there is any error in the socket, it removes the socket from the lists.
    ####
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # remove socket from output array as it has no data
            print(f'Closing connection with {s}')
            outputs.remove(s)
        else:
            # Send message to socket(s)
            s.send(next_msg)

    for s in exceptional:
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]