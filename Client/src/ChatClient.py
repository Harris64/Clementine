import socket

class ChatClient():
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, message):
        self.socket.sendall(message)

        data = self.socket.recv(1024)

        self.socket.close()

        print repr(data)

chatClient = ChatClient("127.0.0.1", 64)
chatClient.send("Hello World!")