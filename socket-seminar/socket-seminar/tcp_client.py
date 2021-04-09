from socket import *
from address_info import SERVER_ADDRESS

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(SERVER_ADDRESS)
print("Connected to server", SERVER_ADDRESS)

message = input().encode('utf-8')
client_socket.sendall(message)

message = client_socket.recv(128).decode('utf-8')

client_socket.close()
print(message)
