import socket

def echo_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Получаем имя хоста
    host = socket.gethostname()
    port = 12345
    
    # Привязываем сокет к заданному адресу и порту
    server_socket.bind((host, port))
    
    # Слушаем до 5 запросов
    server_socket.listen(5)
    
    print(f"Эхо-сервер запущен на {host}:{port}...")
    
    while True:
        # Принимаем подключение
        client_socket, addr = server_socket.accept()
        print(f"Подключено от {addr}")
        
        # Получаем данные от клиента и отправляем обратно
        data = client_socket.recv(1024)
        while data:
            print(f"Получено: {data.decode()}")
            client_socket.send(data)
            data = client_socket.recv(1024)
        
        print("Подключение закрыто")
        client_socket.close()

if __name__ == "__main__":
    echo_server()
