# Normally we would use python built-in library smtplib for sending mail using SMTP protocol

# This program is a simple mail client that sends email to any recipient
# It connects to a mail server and dialogue with the mail server using the SMTP protocol, and send an email message to the mail server

# In order to bypass spam detection, we can send email to AOL mail server or university campus mail server

import socket
from config import EMAIL, PASSWORD

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = "smtp.gmail.com"
port = 587

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
mailFromCommand = f"MAIL FROM: <{EMAIL}>\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in start
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
# Fill in end
# Send DATA command and print server response.
# Fill in start
# Fill in end
# Send message data.
# Fill in start
# Fill in end
# Message ends with a single period.
# Fill in start
# Fill in end
# Send QUIT command and get server response.
# Fill
