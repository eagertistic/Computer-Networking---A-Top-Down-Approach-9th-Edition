from socket import *

serverName = "192.168.1.254"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
outputdata = "GET /index.html HTTP/1.1\r\nHost: 192.168.1.254\r\n\r\n"
clientSocket.send(outputdata.encode())
data = 1

while data:
    data = clientSocket.recv(1024)
    print(data.decode())
clientSocket.close()
