import socket

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    actions = ["l", "r", "t", "b"]
    while True:
        # Получение команды от сервера
        command = client_socket.recv(1024).decode()
        print("Получена команда от сервера:", command)

        # Выполнение команды и отправка результата
        command_parts = command.split(",")
        action = command_parts[0]
        value = int(command_parts[1])
        
        # Выполнение действия в зависимости от команды
        if actions.count(action):
            response = f"Выполнено"
        else:
            response = "Неверная команда"

        # Отправка результата выполнения обратно серверу
        client_socket.sendall(response.encode())
finally:
    # Закрытие соединения
    client_socket.close()
