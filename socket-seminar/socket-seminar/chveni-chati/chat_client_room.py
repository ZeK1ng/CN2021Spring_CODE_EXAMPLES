# 46.101.203.83
from socket import *

room_socket = socket(AF_INET, SOCK_STREAM)
room_socket.connect(('46.101.203.83', 12237))
while True:
    print(room_socket.recv(128).decode('utf-8'))

