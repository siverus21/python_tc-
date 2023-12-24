import socket

def echo_client(message):
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Получаем имя хоста
    host = socket.gethostname()
    port = 12345
    
    # Подключаемся к серверу
    client_socket.connect((host, port))
    
    # Отправляем сообщение серверу
    client_socket.send(message.encode())
    
    # Получаем и выводим ответ от сервера
    data = client_socket.recv(1024)
    print(f"Получено от сервера: {data.decode()}")
    
    # Закрываем соединение
    client_socket.close()

if __name__ == "__main__":
    message = "Привет, сервер! Это сообщение от клиента."
    echo_client(message)
