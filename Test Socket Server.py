#-----------------------------------------------------------------------#
# Name:        Test Socket Server                                       #
# Purpose:     Social-Hub                                               #
#                                                                       #
# Author:      Monty Burrows                                            #
#                                                                       #
# Created:     09/11/2018                                               #
# Copyright:   (c) Monty Burrows 2018                                   #
# Licence:     N/A                                                      #
#-----------------------------------------------------------------------#

import socket                                                           #Imports socket
from threading import *                                                 #Imports all from threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   #SOCK_STREAM opens the TCP socket; AF_INET specifies to use IPv4
host = "localhost"                                                      #Sets IPv4 of server - localhost -> yourself
port = 194                                                              #Sets port to use
print(host+":"+str(port))                                               #For testing purposes, to see if the details to connect are correct
s.bind((host, port))                                                    #Binds values to server

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket                                              #Defining self.sock to socket(s)
        self.addr = address                                             #Defining self.address to address of client
        self.start()                                                    #Start
        
    def run(self):
        while 1:
            global ret
            ret = self.sock.recv(1024).decode()
            print('Client sent: '+ret)
            ret = ret.encode('utf-8')
            self.sock.send(b"You: "+ret)

s.listen(5)
print ('Server online.')
while 1:
    clientsocket, address = s.accept()
    client(clientsocket, address)
