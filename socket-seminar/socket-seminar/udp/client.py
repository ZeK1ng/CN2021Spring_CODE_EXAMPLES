from socket import *

from address_info import SERVER_ADDRESS

message = "asdf".encode('utf-8')
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.sendto(message, SERVER_ADDRESS)
response, server = client_socket.recvfrom(2048)
client_socket.close()
print(response)
