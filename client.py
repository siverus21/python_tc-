# файл client.py
from socket import *
import os
import time

HOST = '127.0.0.1'
PORT = 3000
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(ADDR)

file_names = ["20MB.bin", "50MB.bin", "100MB.bin"]

# Отправляем количество файлов
tcpClientSocket.send(str(len(file_names)).encode())

for name in file_names:
    print(name)
    file_name = name
    file_size = os.path.getsize(f'client_files/{file_name}')
    send_file_size = 0

    tcpClientSocket.send(file_name.encode())
    tcpClientSocket.send(str(file_size).encode())  # Отправляем размер файла

    f = open(f'client_files/{file_name}', 'rb')

    start_time = time.time()

    send_data = ""

    while send_data != b"":
        send_data = f.read(BUFSIZE)
        tcpClientSocket.send(send_data)
        send_file_size += len(send_data)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Time taken for {name}: {elapsed_time} seconds")

tcpClientSocket.close()
