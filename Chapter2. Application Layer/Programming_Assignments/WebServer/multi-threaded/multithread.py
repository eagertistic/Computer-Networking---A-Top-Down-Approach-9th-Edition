from socket import *
import threading
import os

print(gethostbyname(gethostname()))


def handle_client(connectionSocket, addr):
    try:
        print(f"[NEW CONNECTION] {addr} is established.")

        message = connectionSocket.recv(1024)
        if not message:
            return

        request = message.decode("utf-8", errors="ignore")
        print("REQUEST:", request.splitlines())

        filename = request.split()[1].lstrip("/") or "index.html"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, filename)

        try:
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
        except FileNotFoundError:
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
    # Allow quick restart: let us bind() the same IP/port even if previous TCP connections are in TIME_WAIT.
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(5)
    print("Server running on port", serverPort)

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print("Connected to:", addr[0], ":", addr[1])
        thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        thread.start()


if __name__ == "__main__":
    main()
