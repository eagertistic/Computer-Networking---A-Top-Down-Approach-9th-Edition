import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostName = "localhost"
portNumber = 80
clientSocket.settimeout(1)
rtts = []
sent = 10
received = 0

for i in range(1, sent + 1):
    try:
        start_time = time.perf_counter()
        message = f"PING #{i} {time.ctime()}"
        clientSocket.sendto(message.encode(), (hostName, portNumber))
        reply = clientSocket.recv(1024)
        end_time = time.perf_counter()
        rtt = (end_time - start_time) * 1000
        rtts.append(round(rtt, 3))
        received += 1
        print(f"Sequence={i} RTT = {rtt:.3f} ms Reply = {reply.decode()}")
    except socket.timeout:
        print(f"Request timed out at sequence number: {i}")
clientSocket.close()

loss_pct = ((sent - received) / sent) * 100

print("\n--- ping statistics ---")
print(f"maximum rtt is: {max(rtts)}")
print(f"minimum rtt is: {min(rtts)}")
print(f"average rtt is: {round(sum(rtts)/len(rtts),3)}")
print(
    f"{sent} packets transmitted, {received} received, {loss_pct:.1f}% packet loss"
)
