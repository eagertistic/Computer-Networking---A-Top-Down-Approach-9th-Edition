# Normally we would use python built-in library smtplib for sending mail using SMTP protocol

# This program is a simple mail client that sends email to any recipient you can configure in your yaml file
# It connects to a mail server and dialogue with the mail server using the SMTP protocol, and send an email message to the mail server

import socket
from pathlib import Path
from datetime import datetime, UTC
from email.utils import format_datetime, formataddr
from email.message import EmailMessage
import yaml
import ssl
import base64

base_dir = Path(__file__).resolve().parent
config_path = base_dir / "config.yaml"

with open(config_path, "r") as file:
    config = yaml.safe_load(file)

SMTP_config = config["SMTP"]
image_path = base_dir / config["image_path"]

# Create the email
msg = EmailMessage()
msg["Subject"] = SMTP_config["subject"]
msg["From"] = formataddr((SMTP_config["username"], SMTP_config["email"]))
msg["To"] = SMTP_config["recipientEmail"]
msg["Date"] = format_datetime(datetime.now(UTC).replace(microsecond=0),
                              usegmt=True)

msg.set_content(f"""Hi wonderful,

Hope you have a wonderful day! I love you!

Your love,
{SMTP_config["username"]}""")

# Attach the image
with open(image_path, "rb") as file:
    file_data = file.read()
    msg.add_attachment(file_data,
                       maintype="image",
                       subtype="jpeg",
                       filename="Anna.jpg")


def send_email():
    context = ssl.create_default_context()

    def expect(reply, code, step):
        print(reply)
        if not reply.startswith(code):
            raise RuntimeError(f"{step}: expected {code}, got {reply}")

    with socket.create_connection(
        (SMTP_config["gmailServer"], SMTP_config["port"])) as clientSocket:
        with context.wrap_socket(
                clientSocket,
                server_hostname=SMTP_config["gmailServer"]) as Ssocket:

            recv = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv, "220", "initial banner")

            Ssocket.sendall(b"EHLO localhost\r\n")
            recv1 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv1, "250", "EHLO")

            Ssocket.sendall(b"AUTH LOGIN\r\n")
            recv2 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv2, "334", "AUTH LOGIN")

            username = base64.b64encode(SMTP_config["email"].encode())
            Ssocket.sendall(username + b"\r\n")
            recv3 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv3, "334", "username")

            appPassword = base64.b64encode(SMTP_config["password"].encode())
            Ssocket.sendall(appPassword + b"\r\n")
            recv4 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv4, "235", "password/auth success")

            mailFromCommand = f"MAIL FROM:<{SMTP_config['email']}>\r\n"
            Ssocket.sendall(mailFromCommand.encode())
            recv5 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv5, "250", "MAIL FROM")

            rcptCommand = f"RCPT TO:<{SMTP_config['recipientEmail']}>\r\n"
            Ssocket.sendall(rcptCommand.encode())
            recv6 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv6, "250", "RCPT TO")

            Ssocket.sendall(b"DATA\r\n")
            recv7 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv7, "354", "DATA")

            Ssocket.sendall(msg.as_bytes() + b"\r\n.\r\n")
            recv8 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv8, "250", "message accepted")

            Ssocket.sendall(b"QUIT\r\n")
            recv9 = Ssocket.recv(1024).decode("utf-8", errors="replace")
            expect(recv9, "221", "QUIT")


if __name__ == "__main__":
    send_email()
