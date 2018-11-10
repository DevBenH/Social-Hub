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
import socket                                                                   #Imports socket
import sys                                                                      #Imports sys (only used to exit)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           #SOCK_STREAM opens the TCP socket; AF_INET specifies to use IPv4
host = "localhost"                                                              #Sets IPv4 of server - NOTE IT IS SET TO localhost WHICH IS YOURSELF
port = 8000                                                                      #Sets port to use 
print(host+":"+str(port))                                                       #For testing purposes, to see if the details to connect are correct
s.connect((host,port))                                                          #Connect to server using the values in variables
print("Connected to server. Start Chatting!")                                   #Friendly UI?

def tr(str):                                                                    #Defining new function to transmit a string
   s.send(r.encode())                                                           #Send r, encoded
   data = ''                                                                    
   data = s.recv(1024).decode()                                                 #Decoding response from server
   print(data)                                                                  #Displays response to user

while 2:
   r = input()                                                                  #Asking for input to send
   if r == "Exit":
      sys.exit("User request")                                                  #If text is "Exit", exit the program
   else:
      tr(s)                                                                     #If not "Exit", send text to server

s.close ()                                                                      #Close connection
