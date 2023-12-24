# файл server.py
from socket import * # Импорт библиотеки
import os

HOST = '127.0.0.1' # ip хоста
PORT = 3000 # порт хоста
ADDR = (HOST, PORT) # записываем все в одну переменную
BUFSIZE = 1024 # размер буфера 

tcpClientSocket = socket(AF_INET, SOCK_STREAM) # Создание клиента 
tcpClientSocket.connect(ADDR) # устанавливаем подключение

file_name = input('Enter file name: ')
file_size = os.path.getsize(f'client_files/{file_name}')
send_file_size = 0

tcpClientSocket.send(file_name.encode())

f = open(f'client_files/{file_name}', 'rb')

send_data = ""

while send_data != b"":
    send_data = f.read(BUFSIZE)
    tcpClientSocket.send(send_data)
    send_file_size+=len(send_data)
    print(100/(file_size / send_file_size), '%')

tcpClientSocket.close() # Закрываем подключение 