import os, sys
from socket import *
import select

class records(object):
    """This class defines the records"""
    
    #creating objects, init method is called to make film object    
    def __init__(self, message):

        #defining properties of the object:
            #each object of class "records" will have properties
        #each will have it's own number, firstname, surname, username
        self.message=message
    
    #define method on object:
        #method is just a function inside a class
        #self refers to object running the code
    def __str__(self):
        return "%s" %(self.message)
        
if __name__ == '__main__':
    menu=[] #empty list
     #user input


def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                
        
print "Menu"
print "-----"
print "1.Press 1 to send message to server"
print "2.Press 2 to send multiple messages to the server"
print "Q.Press Q to quit"

user=0


user=raw_input("<:  ")

if user=="1":
    host = "127.0.0.1" # set to IP address of target computer
port = 5000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Enter message to send")
    UDPSock.sendto(data, addr)
UDPSock.close()
os._exit(0)

if user=="2":
    broadcast_data()
    
    


if user=="Q":
            print quit()

        

    

       



