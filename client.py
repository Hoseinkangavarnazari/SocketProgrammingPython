import socket
import sys

serverAddr = 'localhost'
serverPort = 4000

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sentence = input('input your sentence: ')
modifiedSentence = clientSocket.recv(1024)
print("Modified sentence received from server : ", modifiedSentence)

