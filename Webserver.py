#import socket module
from socket import *
import sys # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = gethostbyname(gethostname()) # localhost
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(1) # number of connections in queue

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # this accepts the client
    try:
        message = connectionSocket.recv(1024) # 1024 is the receive buffer size
        filename = message.split()[1]
        print(filename)
        f = open(filename[1:])
        print(f)
        outputdata = f.read()
        print(outputdata)
        f.close()
        # Send one HTTP header line into socket 
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) # Ok


        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) 
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        #Close client socket
        connectionSocket.close()
 

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
        
