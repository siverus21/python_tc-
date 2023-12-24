# файл server.py
from socket import * # Импорт библиотеки

HOST = '127.0.0.1' # ip хоста
PORT = 3000 # порт хоста
ADDR = (HOST, PORT) # записываем все в одну переменную
BUFSIZE = 1024 # размер буфера 

tcpServerSocket = socket(AF_INET, SOCK_STREAM) # Создание tcp сервера
tcpServerSocket.bind(ADDR) # Устанавливаем привязку адреса
tcpServerSocket.listen(2) # Устанавливаем ограничение подключений 

tcpClientSocket, addr = tcpServerSocket.accept() #  ожидание подключения клиента

print(tcpClientSocket.recv(BUFSIZE)) # Полученная информация 

tcpServerSocket.close() # Закрываем сервер
tcpClientSocket.close() # Закрываем клиент