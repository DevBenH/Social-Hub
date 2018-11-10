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

import socket
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.71"
port = 194
print(host+":"+str(port))
s.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

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
