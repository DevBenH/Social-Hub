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
host = "192.168.1.71"                                                           #Sets IPv4 of server
port = 194                                                                      #Sets port to use (194 is ICR - Instant Chat Relay)
print(host+":"+str(port))                                                       #For testing purposes, to see if the details to connect are correct
s.connect((host,port))                                                          #Connect to server using the values in variables
print("Connected to server. Start Chatting!")                                   #Friendly UI?

def tr(str):                                                                    #Defining new function to transmit a string
   s.send(r.encode())                                                           #Send r, encoded
   data = ''                                                                    
   data = s.recv(1024).decode()                                                 #Decoding response from server
   print(data)                                                                  #Displays response to user

while 2 True:
   r = input()                                                                  #Asking for input to send
   if r == "Exit":
      2 = False
      sys.exit("User request")                                                  #If text is "Exit", exit the program
   else:
      tr(s)                                                                     #If not "Exit", send text to server
      2 = True

s.close ()                                                                      #Close connection
