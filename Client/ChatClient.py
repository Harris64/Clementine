import socket

# ChatClient class.
class ChatClient:

    # Constructor method.
    def __init__(self, hostAddress, hostPort):

        # Set object attributes.
        self.hostAddress = hostAddress
        self.hostPort = hostPort

    # Initialisation method.
    def initialise(self):

        # Construct socket and bind it.
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.hostAddress, self.hostPort))

        # Set status flag.
        self.status = True

    def pool(self):
        while self.status == True:
            message = raw_input("Message: ")

            if message == "exit":
                self.clientSocket.close()
                
                self.status = False
            else:
                self.clientSocket.send(message)

                response = self.clientSocket.recv(1024)

                print response

chatClient = ChatClient("10.0.74.92", 8888)
chatClient.initialise()
chatClient.pool()
