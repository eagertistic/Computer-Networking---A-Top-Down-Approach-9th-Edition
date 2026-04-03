import random
import socket
import time
import re
import logging

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", 80))
serverSocket.settimeout(3 * 10)

while True:
    rand = random.randint(0, 10)

    try:
        message, address = serverSocket.recvfrom(1024)
    except socket.timeout:
        logging.error("No heartbeat for 30s -> client assumed STOPPED.")
        break

    text = message.decode(errors="ignore")
    trimmed_msg = re.search(r"\bat\s+(\d+(?:\.\d+)?)\b", text)

    start_time = time.time()

    if rand < 4:
        ts = float(trimmed_msg.group(1))  # seconds since epoch
        loss_msg = "packet is lost at " + time.ctime(ts)
        print(loss_msg)
        serverSocket.sendto(loss_msg.encode(), address)
        continue

    time_diff_s = start_time - float(trimmed_msg.group(1))
    time_diff_ms = time_diff_s * 1000
    print(f"{time_diff_ms:.3f} ms")

# The output often shows 0.0, which suggests that the one-way delay measurement may be inaccurate.
# It depends on clock synchronization
# Further improvements may be needed.
