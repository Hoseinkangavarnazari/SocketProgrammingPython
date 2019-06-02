import socket
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 6000
# making a Stream socket on the client side
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the server
clientSocket.connect((SERVER_HOST,SERVER_PORT))

try:
    # do it for ever
    while True:
        # receiving the duration of connection in string 
        durationOfConnection = clientSocket.recv(1024)
        print("Duration of the connection is " , durationOfConnection.decode())

except:
    # if there is a problem close the connection and print error
    clientSocket.close()
    print("There is a problem in connection")