import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = 'localhost'
PORT = 4000

serverSocket.bind((HOST,PORT))

while True:
    data, addr = serverSocket.recvfrom(1024)
    modifiedData = data.upper()
    print ("Message: ", data)
    serverSocket.send(modifiedData,addr)