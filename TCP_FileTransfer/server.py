# Upload some file into the server from the client

import socket
import sys

# Define a new socket with IPv4 / SOCK_STREAM (A.K.A TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


HOST = "localhost"
PORT = 9998

# binding the above configuration into the server
s.bind((HOST, PORT))
# listen to i client without accept until refusing another request
s.listen(5)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("Client connected with Port:", addr)

    # get file name to download
    file = open("received.mp3", "wb")
    while True:
        # get file bytes, set the buffer size
        # receving files in 4096kb chunks
        # i have changed the value but i didn't see noticiable change in it
        data = conn.recv(4096)

        # if there is nothing left to receive break the loop
        if not data:
            break
        # write bytes on file
        file.write(data)
    # closing the file, from this line of code, it's safe to use the received file
    file.close()
    print("File Downloaded.")

    # close connection
    conn.close()
    print("Connection Closed")
    
    #  a clean exit without any errors
    sys.exit(0)