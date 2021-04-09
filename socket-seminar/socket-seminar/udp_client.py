from socket import *

from address_info import SERVER_ADDRESS
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    client_socket.sendto(input("enter message:").encode('utf-8'), SERVER_ADDRESS)
