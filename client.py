import socket
import sys

serverAddr = 'localhost'
serverPort = 4000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('input your sentence: ')
    clientSocket.sendto(msg.encode(), (serverAddr, serverPort))
    modifiedSentence, serverAddr = clientSocket.recvfrom(1024)
    print("Modified sentence received from server : ", modifiedSentence.decode())
