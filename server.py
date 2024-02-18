import socket
from command import *
import time

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Связывание сокета с адресом и портом
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Начало прослушивания входящих соединений
server_socket.listen(1)

print("Ждем подключения клиента...")

# Принятие входящего соединения
client_socket, client_address = server_socket.accept()
print("Подключен клиент:", client_address)

try:
    height_now = CONST_START_HEIGHT # стартовая высота 
    position_is_left = True
    while height_now != CONST_END_HEIGHT: # пока текущая высота не вышла за пределы высоты скважины, будем долбить
        angle_now = CONST_ANGLE_START # cтартовый угол
        while angle_now <= CONST_ANGLE_END: # пока угол камеры не упрется в конец, также долбим

            client_socket.sendall(Photo().encode()) # делаем фото ( улыбочку:) )
            response = client_socket.recv(1024).decode() # принимаем, что все окей

            if CheckResponse(response) != "OK": # проверяем, точно ли все ок? если нет, то вылатеам с циклов 
                break

            time.sleep(0.3)  # Добавляем задержку в 1 секунду, чтобы все было плавно (это на данном этапе)
            if(position_is_left):
                client_socket.sendall(Right_step(defaul_step).encode()) # крутимся вправо на 30 градусов
            else:
                client_socket.sendall(Left_step(defaul_step).encode())

            response = client_socket.recv(1024).decode() # принимаем, что все ок

            if CheckResponse(response) != "OK": # проверяем, точно ли все ок? если нет, то вылатеам с циклов
                break
            else:
                angle_now += defaul_step # если все отлично, то изменяем текущее положение дел и меняем значение текущего градуса 
                print(angle_now)

            time.sleep(0.3)  # Добавляем задержку в 1 секунду

        if response != "OK": # Если все не очень хорошо, то ломаем лицо циклу
            client_socket.sendall(Up_step(abs(height_now)).encode())

        position_is_left = not position_is_left

        if(height_now == CONST_END_HEIGHT - 1):
            print("END")   
            break
        else:
            height_now += 1
            client_socket.sendall(Up_step(height_now).encode())
            response = client_socket.recv(1024).decode()
finally:
    time.sleep(1)
    # Закрытие соединения
    # client_socket.close()
    server_socket.close()
