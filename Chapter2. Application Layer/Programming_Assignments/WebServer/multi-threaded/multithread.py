from socket import *
import threading
import os
from _thread import start_new_thread

lock = threading.Lock()
print(gethostbyname(gethostname()))

def handle_connection(connectionSocket):
    while True:
        try:
            message = connectionSocket.recv(1024)
            if not message:
                connectionSocket.close()
                lock.release()
                break
            request = message.decode("utf-8", errors="ignore")
            print("REQUEST:", request.splitlines())
            filename = request.split()[1].lstrip("/") or "index.html"
            base_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base_dir, filename)

            with open(path, "rb") as f:
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


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(5)
    print("Server running on port", serverPort)

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        lock.acquire()
        print("Connected to:", addr[0], ":", addr[1])
        start_new_thread(handle_connection, (connectionSocket,))


if __name__ == "__main__":
    main()
