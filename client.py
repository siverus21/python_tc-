import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        # Отправка сообщения серверу
        message = input("сообщение для Сервера: ")
        client_socket.sendall(message.encode())

        # Получение ответа от сервера
        data = client_socket.recv(1024)
        if data:
            print("Сервер:", data.decode())
finally:
    # Закрытие соединения
    client_socket.close()
