import socket
import errno  # Импортируем модуль errno
from command import *
import time

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        try:
            command = client_socket.recv(1024).decode()
            print("Получена команда от сервера:", command)

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
        try:
            client_socket.sendall(response.encode())
        except socket.error as e:
            if e.errno == errno.EPIPE:
                print("Соединение было разорвано")
                break
finally:
    client_socket.close()
