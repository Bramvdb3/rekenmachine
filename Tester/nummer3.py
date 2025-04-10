import socket
host = socket.gethostbyname(socket.gethostname())
port = 9089
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f'Connected to {address}')
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from client is: {message}')
    communication_socket.send(f'Got your message! Thank you!'.encode('utf-8'))
    communication_socket.close()
    print(f'Connection with {address} ended!'.decode(utf-8))
    
