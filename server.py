import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = 'localhost'
PORT = 4000

serverSocket.bind((HOST,PORT))

while True:
    data, addr = serverSocket.recvfrom(1024)
    modifiedData = str(data.decode()).upper()
    print ("Message: ", data.decode())
    print(modifiedData)
    serverSocket.sendto(modifiedData.encode(),addr)