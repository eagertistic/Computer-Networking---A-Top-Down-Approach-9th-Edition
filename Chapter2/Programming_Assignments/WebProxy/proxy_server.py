import socket
import os
from urllib.parse import urlparse
import hashlib

serverPort = 8000

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpSerSock.bind(("localhost", serverPort))
tcpSerSock.listen(1)

print(f"Proxy running on localhost:{serverPort}")

os.makedirs("cache", exist_ok=True)
cache = {}


def get_cache_filename(cache_key):
    name = hashlib.sha256(cache_key.encode("utf-8")).hexdigest()
    return "cache/" + name + ".cache"


while True:
    c = None
    tcpCliSock, addr = tcpSerSock.accept()

    try:
        print("Ready to serve...")
        print("Received a connection from:", addr)

        raw_message = tcpCliSock.recv(4096)

        if not raw_message:
            continue

        message = raw_message.decode("utf-8", errors="ignore")
        print(message)

        if "\r\n\r\n" in message:
            headers_part, body = message.split("\r\n\r\n", 1)
        else:
            headers_part = message
            body = ""

        lines = headers_part.splitlines()
        request_line = lines[0]

        method, target_url, version = request_line.split()

        if method not in ("GET", "POST"):
            tcpCliSock.sendall(b"HTTP/1.0 501 Not Implemented\r\n\r\n")
            continue

        hostname = ""
        content_type = ""

        for line in lines[1:]:
            if line.lower().startswith("host:"):
                hostname = line.split(":", 1)[1].strip()
                break

        for line in lines[1:]:
            if line.lower().startswith("content-type:"):
                content_type = line + "\r\n"
                break

        parsed_url = urlparse(target_url)

        if parsed_url.scheme and parsed_url.netloc:
            # Example: # GET http://example.com/index.html HTTP/1.1
            hostname = parsed_url.netloc
            path = parsed_url.path or "/"

            if parsed_url.query:
                path += "?" + parsed_url.query
        else:
            # extract path for example: /index.html
            path = target_url or "/"

        hostname = hostname.split(":", 1)[0]

        if not hostname:
            tcpCliSock.sendall(
                b"HTTP/1.0 400 Bad Request\r\n\r\nMissing Host header")
            continue

        cache_key = hostname + path

        if method == "POST":
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((hostname, 80))

            request_body = body.encode("utf-8")

            request_headers = (f"POST {path} HTTP/1.0\r\n"
                               f"Host: {hostname}\r\n"
                               f"{content_type}"
                               f"Content-Length: {len(request_body)}\r\n"
                               f"Connection: close\r\n"
                               f"\r\n").encode("utf-8")

            c.sendall(request_headers + request_body)

            response = b""
            while True:
                data = c.recv(2048)
                if not data:
                    break
                response += data

            tcpCliSock.sendall(response)
            continue

        if method == "GET":
            if cache_key in cache:
                filename = cache[cache_key]

                try:
                    with open(filename, "rb") as f:
                        outputdata = f.read()

                    tcpCliSock.sendall(outputdata)
                    print("Read from cache")
                    continue

                except IOError:
                    del cache[cache_key]

            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((hostname, 80))

            request = (f"GET {path} HTTP/1.0\r\n"
                       f"Host: {hostname}\r\n"
                       f"Connection: close\r\n"
                       f"\r\n").encode("utf-8")

            c.sendall(request)

            buffer = b""
            while True:
                data = c.recv(2048)
                if not data:
                    break
                buffer += data

            tcpCliSock.sendall(buffer)

            status_line = buffer.split(b"\r\n", 1)[0]

            if b"200 OK" in status_line:
                filename = get_cache_filename(cache_key)

                with open(filename, "wb") as tmpFile:
                    tmpFile.write(buffer)

                cache[cache_key] = filename

                with open("cache/index.txt", "a") as index:
                    index.write(f"{cache_key} -> {filename}\n")
                print("Saved to cache")

            continue

    except Exception as e:
        print("Illegal request:", e)

    finally:
        if c:
            c.close()
        tcpCliSock.close()
