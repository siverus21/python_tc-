import socket

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Связывание сокета с адресом и портом
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Начало прослушивания входящих соединений
server_socket.listen(1)

print("Ждем подключения клиента...")

# Принятие входящего соединения
client_socket, client_address = server_socket.accept()
print("Подключен клиент:", client_address)

try:
    while True:
        # Получение сообщения от клиента
        data = client_socket.recv(1024)
        if data:
            print("Клиент:", data.decode())

            # Отправка ответа клиенту
            message = input("Сообщение для клиента: ")
            client_socket.sendall(message.encode())
finally:
    # Закрытие соединения
    client_socket.close()
    server_socket.close()
