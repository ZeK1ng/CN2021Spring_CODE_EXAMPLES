# 46.101.203.83
from socket import *

messenger_socket = socket(AF_INET, SOCK_STREAM)
messenger_socket.connect(('46.101.203.83', 12238))
messenger_socket.sendall("ping ping".encode('utf-8'))
messenger_socket.close()

