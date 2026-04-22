import socket
from urllib.parse import urlparse

# Create a server socket, bind it to a port and start listening
serverPort = 8000
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSerSock.bind(("localhost", serverPort))
tcpSerSock.listen(1)

print(f"Proxy running on localhost:{serverPort}")

while 1:
    c = None
    tcpCliSock, addr = tcpSerSock.accept()

    try:
        print('Ready to serve...')
        print('Received a connection from:', addr)

        message = tcpCliSock.recv(1024).decode("utf-8", errors="ignore")
        print(message)

        lines = message.splitlines()
        request_line = lines[0]
        method, target_url, version = request_line.split()
        hostname = ""

        for line in lines:
            if line.startswith("Host:"):
                hostname = line.split(":", 1)[1].strip()
                break

        hostname = hostname.split(":", 1)[0]

        if method != "GET":
            tcpCliSock.sendall(b"HTTP/1.0 501 Not Implemented\r\n\r\n")
            continue

        parsed_url = urlparse(target_url)
        # extract path /index.html
        path = parsed_url.path or "/"
        filename = path.split("/")[-1] or "index.html"

        try:
            # Check wether the file exist in the cache
            with open(filename, "rb") as f:
                outputdata = f.read()

            # ProxyServer finds a cache hit and generates a response message
            tcpCliSock.sendall(outputdata)

            print('Read from cache')

        # Error handling for file not found in cache
        except IOError:
            # Create a socket on the proxyserver
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the socket to port 80
            c.connect((hostname, 80))
            request = "GET " + path + " HTTP/1.0\r\nHost: " + hostname + "\r\n\r\n"
            c.sendall(request.encode())
            buffer = b""
            while True:
                data = c.recv(2048)
                if not data:
                    break
                buffer += data
            # # Also send the response in the buffer to client socket
            tcpCliSock.sendall(buffer)
            status_line = buffer.split(
                b"\r\n", 1
            )[0]  # check if the response is successful and create a cached file
            if b"200 OK" in status_line:
                with open("./" + filename, "wb") as tmpFile:
                    tmpFile.write(buffer)
    except Exception:
        print("Illegal request")

    finally:
        if c:
            c.close()
        tcpCliSock.close()

tcpSerSock.close()
