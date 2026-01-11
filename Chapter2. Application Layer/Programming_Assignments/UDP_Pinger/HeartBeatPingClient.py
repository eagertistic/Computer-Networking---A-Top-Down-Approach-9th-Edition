import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverName = "localhost"
portNumber = 80

for i in range(1, 11):
    msg = f"Sequence number:{i} at {time.time()}"
    clientSocket.sendto(msg.encode(), (serverName, portNumber))
    time.sleep(1)

