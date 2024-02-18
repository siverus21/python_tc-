import socket
from command import *
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)

print("Ждем подключения клиента...")

client_socket, client_address = server_socket.accept()
print("Подключен клиент:", client_address)

try:
    height_now = CONST_START_HEIGHT
    position_is_left = True
    while height_now != CONST_END_HEIGHT:
        angle_now = CONST_ANGLE_START
        while angle_now <= CONST_ANGLE_END:

            client_socket.sendall(Photo().encode())
            response = client_socket.recv(1024).decode()

            if CheckResponse(response) != "OK":
                break

            # time.sleep(0.3)
            if(position_is_left):
                client_socket.sendall(Right_step(defaul_step).encode())
            else:
                client_socket.sendall(Left_step(defaul_step).encode())

            response = client_socket.recv(1024).decode()

            if CheckResponse(response) != "OK":
                break
            else:
                angle_now += defaul_step
                print(angle_now)

            # time.sleep(0.3)

        if response != "OK":
            client_socket.sendall(Up_step(abs(height_now)).encode())

        position_is_left = not position_is_left

        if(height_now == CONST_END_HEIGHT - 1):
            client_socket.sendall(EndProgram().encode())
            break
        else:
            height_now += 1
            client_socket.sendall(Up_step(height_now).encode())
            response = client_socket.recv(1024).decode()
finally:
    time.sleep(1)
    client_socket.close()
    server_socket.close()
