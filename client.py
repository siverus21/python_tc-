# файл server.py
from socket import * # Импорт библиотеки

HOST = '127.0.0.1' # ip хоста
PORT = 3000 # порт хоста
ADDR = (HOST, PORT) # записываем все в одну переменную
BUFSIZE = 1024 # размер буфера 

tcpClientSocket = socket(AF_INET, SOCK_STREAM) # Создание клиента 
tcpClientSocket.connect(ADDR) # устанавливаем подключение

tcpClientSocket.send('HELLO'.encode()) # Передаем сообщение 

tcpClientSocket.close() # Закрываем подключение 