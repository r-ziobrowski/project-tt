import socket
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

UDP_IP = "192.168.1.10"
UDP_PORT = 5005
MESSAGE = b"Hello World!"

print(f"UDP target IP: {UDP_IP}")
print(f"UDP target port: {UDP_PORT}")
print(f"Message: {dt_string}")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(dt_string.encode(), (UDP_IP, UDP_PORT))
