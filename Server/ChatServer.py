import socket

class ChatServer:
    def __init__(self, hostAddress, hostPort):
        self.hostAddress = hostAddress
        self.hostPort = hostPort
    
    def initialise(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.hostAddress, self.hostPort))
        self.serverSocket.listen(8)

        self.status = True

    def acceptConnections(self):
        while self.status == True:
            connection, address = self.serverSocket.accept()
            data = connection.recv(1024)

            if data != None:
                connection.send(data)

            connection.close()
        else:
            self.terminate()

    def terminate(self):
        self.serverSocket.close()

chatServer = ChatServer("127.0.0.1", 1234)
chatServer.initialise()
chatServer.acceptConnections()
