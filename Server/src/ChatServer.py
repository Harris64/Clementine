import socket

class ChatServer():
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

    def listen(self):
        self.socket.listen(1)

        connection, address = self.socket.accept()

        while True:
            data = connection.recv(1024)

            if not data:
                break

            connection.sendall(data)

        connection.close()

chatServer = ChatServer("", 64)
chatServer.listen()
