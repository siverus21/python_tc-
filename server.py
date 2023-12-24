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

file_name = tcpClientSocket.recv(BUFSIZE).decode()

f = open(f'server_files/{file_name}', 'wb')

while True:
    taked_data = tcpClientSocket.recv(BUFSIZE)
    if not taked_data:
        break
    f.write(taked_data)

    
tcpServerSocket.close() # Закрываем сервер
tcpClientSocket.close() # Закрываем клиент