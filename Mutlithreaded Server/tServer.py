import socket
import sys
from _thread import *
import time


def responseThread(client,threadName):
    counter = 0
    try:
        while True:
            print("Thread ",threadName,"Send the duration of connection to the client")
            client.send(str(counter).encode())
            time.sleep(60)
            counter +=1
    except:
        print("There is a problem with client")
        client.close()


def main():
    # configuration
    SERVER_HOST = 'localhost'
    SERVER_PORT = 6000
    # defining type of the socket / IPv4 and TCP
    # AF_INET : specifies address family,
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binds the aformentioned congiguration to above socket
    serverSocket.bind((SERVER_HOST, SERVER_PORT))

    # specifies how many unaccepted connections request are allowed befor rejecting the new ones
    # in this case it is equal to 5, actually for our case it doesn't matter
    serverSocket.listen(5)
    print("Server is ready ... on port ", SERVER_PORT)

    threadCounter = 1
    while True:
        connectionSocket, addr = serverSocket.accept()
        # make here the thread
        start_new_thread(responseThread, (connectionSocket,threadCounter)) 
        threadCounter +=1

if __name__ == '__main__':
    main()
