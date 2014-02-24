import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 80

size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))
client.send("Testing...")

data = client.recv(size)

client.close()

print data
