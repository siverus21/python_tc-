import socket

# Словарь с описаниями функций
help_text = {
    "l": "Переместить объект влево на указанное количество градусов.",
    "r": "Переместить объект вправо на указанное количество градусов.",
    "t": "Переместить объект вверх на указанное количество градусов.",
    "b": "Переместить объект вниз на указанное количество градусов.",
    "help": "Показать список доступных команд и их описания."
}

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
        # Получение команды от пользователя
        str_input = input(">>>")
        
        # Разбиение введенной строки на команду и аргументы
        command, *args = str_input.split(",")

        # Обработка команды help
        if command == "help":
            # Вывод списка доступных команд и их описания
            for cmd, desc in help_text.items():
                print(f"{cmd}: {desc}")
            continue

        # Проверка наличия команды в списке доступных команд
        if command not in help_text:
            print("Неверная команда.")
            continue

        # Отправка команды клиенту
        client_socket.sendall(str_input.encode())

        # Получение результата от клиента
        response = client_socket.recv(1024).decode()
        print("Ответ:", response)
finally:
    # Закрытие соединения
    client_socket.close()
    server_socket.close()
