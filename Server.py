import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 80

backlog = 5
size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_ADDRESS, SERVER_PORT))
server.listen(backlog)

while True:
    client, address = server.accept()
    data = client.recv(size)

    if data != "":
        client.send(data)

    client.close()
