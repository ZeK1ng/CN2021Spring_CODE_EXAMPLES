from socket import *

from address_info import SERVER_ADDRESS


server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)
print("Server is running on", SERVER_ADDRESS)
while True:
    print("Waiting for data")
    message, client_address = server_socket.recvfrom(128)
    print("Message received", message.decode('utf-8'))
    server_socket.sendto(message, client_address)



