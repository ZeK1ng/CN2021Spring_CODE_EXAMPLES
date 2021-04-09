from socket import *
from threading import Thread
# from addrs import BROADCAST_ADDRESS, MESSAGE_ADDRESS

BROADCAST_ADDRESS = ('0.0.0.0', 12237)
MESSAGE_ADDRESS = ('0.0.0.0', 12238)
# Broadcast
connections = {}

broadcast_socket = socket(AF_INET, SOCK_STREAM)
broadcast_socket.bind(BROADCAST_ADDRESS)
broadcast_socket.listen(1000)
print("Broadcast server started listening on", BROADCAST_ADDRESS)


def handle_broadcast_connections():
    while True:
        _socket, addr = broadcast_socket.accept()
        print("New client", addr, "connected")
        connections[addr] = _socket


Thread(target=handle_broadcast_connections, args=()).start()

# Message
message_socket = socket(AF_INET, SOCK_STREAM)
message_socket.bind(MESSAGE_ADDRESS)
message_socket.listen(1000)
print("Message server started listening on", MESSAGE_ADDRESS)


def do_work(_socket):
    message = _socket.recv(128)
    print("New message:", message, "received, Broadcasting !!!!")
    for sock_addr in connections:
        try:
            connections[sock_addr].sendall(message)
        except Exception as e:
            print(e)
    _socket.close()


while True:
    _socket, addr = message_socket.accept()
    Thread(target=do_work, args=(_socket,)).start()
