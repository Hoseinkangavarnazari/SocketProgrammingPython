import socket
import sys

# configuration 
SERVER_HOST = 'localhost'
SERVER_PORT = 6000
# defining type of the socket / IPv4 and TCP
# AF_INET : specifies address family,
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binds the aformentioned congiguration to above socket
serverSocket.bind((SERVER_HOST, SERVER_PORT))

# specifies how many unaccepted connections request are allowed befor rejecting the new ones
# in this case it is equal to 2, actually for our case it doesn't matter
serverSocket.listen(2)

print("Server is ready ... on port ", SERVER_PORT)
# server accepts the connection and receives information about the receivers
connectionSocket, addr = serverSocket.accept()
# we can print to see address of the client
while True:
    # connectionSocket chuncks
    data = connectionSocket.recv(1024)
    # decode the data from binary to cast it into string, then we can use the uppercase function
    modifiedData = str(data.decode()).upper()
    print("Message: ", modifiedData)
    connectionSocket.send(modifiedData.encode())

connectionSocket.close()

