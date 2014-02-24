import socket

SERVER_ADDRESS = "109.175.132.136"
SERVER_PORT = 1234

size = 1024
sendText= raw_input("please type your message: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_ADDRESS, SERVER_PORT))
client.send(sendText)

data = client.recv(size)

client.close()

print data
