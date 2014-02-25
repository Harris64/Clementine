import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 8888

a=1

while a == 1:
    size = 1024
    Chat = raw_input("Enter text to send to chat: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_ADDRESS, SERVER_PORT))
    client.send(Chat)

    data = client.recv(size)

    print data

    if Chat == "exit":
        print "Goodbye"
        a=0
        

client.close()

