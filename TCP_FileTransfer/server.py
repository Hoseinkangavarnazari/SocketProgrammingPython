# Upload some file into the server from the client

import socket
import sys


HOST = "localhost"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
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
        data = conn.recv(4096)

        # if there is nothing left to receive break the loop
        if not data:
            break
        # write bytes on file
        file.write(data)
    file.close()
    print("File Downloaded.")

    # close connection
    conn.close()
    print("Connection Closed")
    sys.exit(0)