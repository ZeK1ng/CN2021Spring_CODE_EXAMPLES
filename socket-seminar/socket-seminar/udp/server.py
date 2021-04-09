from socket import *

from address_info import SERVER_ADDRESS

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)

while True:
    print("Waiting for data +_+")
    message, addr = server_socket.recvfrom(2048)
    print("New message", message, 'from', addr)
    server_socket.sendto(message.decode('utf-8').upper().encode('utf-8'), addr)
