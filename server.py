import socket
from command import *
import time

def initialize_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Ждем подключения клиента...")
    client_socket, client_address = server_socket.accept()
    print("Подключен клиент:", client_address)
    return server_socket, client_socket

def receive_command(client_socket):
    try:
        command = client_socket.recv(1024).decode()
        print("Получена команда от сервера:", command)
        return command
    except:
        return 'error'

def send_response(client_socket, response):
    try:
        client_socket.sendall(response.encode())
    except socket.error as e:
        if e.errno == errno.EPIPE:
            print("Соединение было разорвано")

def close_connections(server_socket, client_socket):
    time.sleep(1)
    client_socket.close()
    server_socket.close()

def run_camera_control_server():
    server_socket, client_socket = initialize_server()
    try:
        height_now = CONST_START_HEIGHT
        position_is_left = True
        while height_now <= CONST_END_HEIGHT:
            angle_now = CONST_ANGLE_START
            while angle_now <= CONST_ANGLE_END:
                client_socket.sendall(Photo().encode())
                response = client_socket.recv(1024).decode()
                if CheckResponse(response) != "OK":
                    break
                if position_is_left:
                    client_socket.sendall(Right_step(DEFAULT_STEP).encode())
                else:
                    client_socket.sendall(Left_step(DEFAULT_STEP).encode())
                response = client_socket.recv(1024).decode()
                if CheckResponse(response) != "OK":
                    break
                else:
                    angle_now += DEFAULT_STEP
                    print(angle_now)
            if response != "OK":
                client_socket.sendall(Up_step(abs(height_now)).encode())
            position_is_left = not position_is_left
            if height_now == CONST_END_HEIGHT:
                client_socket.sendall(EndProgram().encode())
                break
            else:
                height_now += 1
                client_socket.sendall(Up_step(height_now).encode())
                response = client_socket.recv(1024).decode()
        print(height_now)
    finally:
        close_connections(server_socket, client_socket)

# Вызовем функцию для запуска сервера
run_camera_control_server()
