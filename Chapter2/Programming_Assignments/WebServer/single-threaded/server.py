from socket import *
import os

print(gethostbyname(gethostname()))

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
# Prepare a sever socket
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        if not message:
            connectionSocket.close()
            continue

        request = message.decode("utf-8", errors="ignore")
        print("REQUEST:", request.splitlines())
        filename = request.split()[1].lstrip("/") or "index.html"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, filename)

        with open(path,"rb") as f:
            body = f.read()

        header = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode("utf-8")
        connectionSocket.sendall(header + body)
        print("OK!")
    except IOError:
        body = b"404 Not Found"
        header = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {len(body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        ).encode("utf-8")
        connectionSocket.sendall(header + body)
    finally:
        connectionSocket.close()
