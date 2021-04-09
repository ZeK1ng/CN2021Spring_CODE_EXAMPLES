from socket import *
from threading import Thread

from address_info import SERVER_ADDRESS

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(SERVER_ADDRESS)

server_socket.listen()


def serve_client(_socket, addr):
    _socket.settimeout(5)
    response = str(int(_socket.recv(128).decode('utf-8')) * 2).encode('utf-8')
    _socket.sendall(response)
    _socket.close()


while True:
    _socket, client_address = server_socket.accept()
    tmp_thread = Thread(target=serve_client, args=(_socket, client_address))
    tmp_thread.start()