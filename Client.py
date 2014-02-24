import socket

SERVER_ADDRESS = "harris64.no-ip.biz"
SERVER_PORT = 1234

size = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))
client.send("Testing...")

data = client.recv(size)

client.close()

print data
