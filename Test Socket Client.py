#-------------------------------------------------------------------------------#
# Name:        Test Socket Client                                               
# Purpose:     Github Task
#
# Author:      Monty Burrows
#
# Created:     09/11/2018
# Copyright:   (c) Monty Burrows 2018
# Licence:     N/A
#-------------------------------------------------------------------------------#
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.71"
port = 194
print(host+":"+str(port))
s.connect((host,port))
print("Connected to server. Start Chatting!")

def tr(str):
   s.send(r.encode())
   data = ''
   data = s.recv(1024).decode()
   print(data)

while 2:
   r = input()
   if r == "Exit":
      sys.exit("User request")
   else:
      tr(s)


s.close ()
