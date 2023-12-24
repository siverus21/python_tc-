import socket
import os

def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Получаем имя хоста
    host = socket.gethostname()
    port = 12345
    
    # Привязываем сокет к заданному адресу и порту
    server_socket.bind((host, port))
    
    # Слушаем до 5 запросов
    server_socket.listen(5)
    
    print(f"Ждем подключения на {host}:{port}...")
    
    while True:
        # Принимаем подключение
        client_socket, addr = server_socket.accept()
        print(f"Подключено от {addr}")
        
        # Принимаем имя файла
        file_name = client_socket.recv(1024).decode()
        
        # Принимаем и сохраняем файл
        with open(file_name, 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                f.write(data)
        
        print(f"Файл '{file_name}' успешно получен")
        client_socket.close()

if __name__ == "__main__":
    start_server()
