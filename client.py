import socket

def send_file(file_path):
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Получаем имя хоста
    host = socket.gethostname()
    port = 12345
    
    # Подключаемся к серверу
    client_socket.connect((host, port))
    
    # Отправляем имя файла
    file_name = os.path.basename(file_path)
    client_socket.send(file_name.encode())
    
    # Отправляем файл
    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)
    
    print(f"Файл '{file_name}' успешно отправлен")
    client_socket.close()

if __name__ == "__main__":
    file_path = "путь_к_вашему_файлу"
    send_file(file_path)
