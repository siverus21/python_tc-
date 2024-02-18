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
        try:
            command = client_socket.recv(1024).decode()
            print("Получена команда от сервера:", command)        
            if command != "photo": # Проверяем, фотокают ли нас 
                # Выполнение команды и отправка результата
                # если нет, то разделяем значения 
                # в action кладем действие
                # в value угол
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
        # Отправка результата выполнения обратно серверу
        # Шлем красную шапочку относить пирожки серваку
        try:    # заменить на что-то вроде if socket.is_open:
            client_socket.sendall(response.encode())
        except:
            print("Соединение было разорвано")
            break

finally:
    # Закрытие соединения
    client_socket.close()
