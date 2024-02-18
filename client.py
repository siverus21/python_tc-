import socket
import errno 
from command import *

def initialize_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    return client_socket

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

def close_connection(client_socket):
    client_socket.close()

def run_client():
    client_socket = initialize_client()
    try:
        while True:
            try:
                command = receive_command(client_socket)

                if command == "END":
                    print("Получена команда завершения от сервера.")
                    break

                if command != "photo":
                    command_parts = command.split(",")
                    action = command_parts[0]
                    try:
                        value = int(command_parts[1])
                    except:
                        response = "Указанное значение не является числом!"

                    if action in commands:
                        response = "OK"
                    else:
                        response = "Неверная команда"
                elif command == "photo":
                    response = "OK"
            except:
                response = 'error'
            send_response(client_socket, response)
    finally:
        close_connection(client_socket)

run_client()
