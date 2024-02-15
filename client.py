import socket
from command import *
import time

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        # Получение команды от сервера
        command = client_socket.recv(1024).decode()
        print("Получена команда от сервера:", command)
        
        if command != "photo": # Проверяем, фотокают ли нас 
            # Выполнение команды и отправка результата
            # если нет, то разделяем значения 
            # в action кладем действие
            # в value угол
            command_parts = command.split(",")
            action = command_parts[0]
            value = int(command_parts[1])

            if action in commands:
                response = "OK"
            else:
                response = "Неверная команда"
        elif command == "photo":
            response = "OK"

        # Отправка результата выполнения обратно серверу
        # Шлем красную шапочку относить пирожки серваку
        client_socket.sendall(response.encode())
finally:
    # Закрытие соединения
    client_socket.close()
