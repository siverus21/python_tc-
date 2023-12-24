# файл server.py
from socket import *
import time

HOST = '127.0.0.1'
PORT = 3000
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(ADDR)
tcpServerSocket.listen(2)

tcpClientSocket, addr = tcpServerSocket.accept()

# Получаем количество файлов
num_files = int(tcpClientSocket.recv(BUFSIZE).decode())

for _ in range(num_files):
    # Получаем байты без декодирования
    file_name = tcpClientSocket.recv(BUFSIZE).strip()

    # Получаем размер файла
    file_size = int(tcpClientSocket.recv(BUFSIZE).decode())

    if file_size == 0:
        print(f"File {file_name.decode()} is empty.")
        continue

    # Открываем файл в бинарном режиме
    file_path = f'server_files/{file_name.decode()}'
    f = open(file_path, 'wb')

    start_time = time.time()  # Засекаем время начала получения файла

    while file_size > 0:
        taked_data = tcpClientSocket.recv(BUFSIZE)
        if not taked_data:
            break
        f.write(taked_data)
        file_size -= len(taked_data)

    end_time = time.time()  # Засекаем время завершения получения файла

    print(f"Time taken to receive {file_path}: {end_time - start_time} seconds")

tcpServerSocket.close()
tcpClientSocket.close()
