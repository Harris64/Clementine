import socket

# ChatServer class.
class ChatServer:

    # Constructor method.
    def __init__(self, hostAddress, hostPort):

        # Set object attributes.
        self.hostAddress = hostAddress
        self.hostPort = hostPort

    # Initialisation method.
    def initialise(self):

        # Construct socket, bind it and start listening.
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.hostAddress, self.hostPort))
        self.serverSocket.listen(8)

        # Set status flag.
        self.status = True

    # Main loop method.
    def acceptConnections(self):

        # Check status flag.
        while self.status == True:

            # Receive connection and read data.
            connection, address = self.serverSocket.accept()
            data = connection.recv(1024)

            # Check if data exists.
            if data != None:

                # Send data back.
                connection.send(data)

            # Close connection.
            connection.close()
        else:

            # Terminate server.
            self.terminate()

    # Terminate method.
    def terminate(self):

        # Close server socket.
        self.serverSocket.close()

chatServer = ChatServer("127.0.0.1", 8888)
chatServer.initialise()
chatServer.acceptConnections()
