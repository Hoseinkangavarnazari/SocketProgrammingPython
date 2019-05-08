import socket
import sys


HOST = "localhost"
PORT = 9999

clinetSocket = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
clinetSocket.connect((HOST, PORT))
print("Connected to the Server")

# address the file that you want to send
f_send = "Billie_Jean.mp3"
# open file and read it as bytes
with open(f_send, "rb") as file:
    # send file
    print("Sending file ...")
    # read the whole file at once
    data = file.read()
    # Convert the file into smaller segments and send them
    clinetSocket.sendall(data)

    # close connection
    clinetSocket.close()
    print("Client connection closed.")
    sys.exit(0)