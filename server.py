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
    '''
        беру изначально стандартное положение
        нужно обдумать, как это можно обыграть, но пока остановимся на этом
        т.е это будет самый низ и левое положение камеры 
    '''  
    height_now = CONST_START_HEIGHT # стартовая высота 
    angle_now = CONST_ANGLE_START # cтартовый угол

    while height_now != CONST_END_HEIGHT: # пока текущая высота не вышла за пределы высоты скважины, будем долбить
        while angle_now != CONST_ANGLE_END: # пока угол камеры не упрется в конец, также долбим
            client_socket.sendall(Photo().encode()) # делаем фото ( улыбочку:) )
            response = client_socket.recv(1024).decode() # принимаем, что все окей

            if CheckResponse(response) != "OK": # проверяем, точно ли все ок? если нет, то вылатеам с циклов 
                break

            print(response) # выводим ответ
            time.sleep(1)  # Добавляем задержку в 1 секунду, чтобы все было плавно (это на данном этапе)

            client_socket.sendall(Right_step(angle_now + defaul_step).encode()) # крутимся вправо на 30 градусов 
            response = client_socket.recv(1024).decode() # принимаем, что все ок

            if CheckResponse(response) != "OK": # проверяем, точно ли все ок? если нет, то вылатеам с циклов
                break
            else:
                angle_now += defaul_step # если все отлично, то изменяем текущее положение дел и меняем значение текущего градуса 

            print(response)
            time.sleep(1)  # Добавляем задержку в 1 секунду

        if response != "OK": # Если все не очень хорошо, то ломаем лицо циклу
            break

        height_now += 1 # тут пока что затычка, потом допишу 

        '''
        Теперь после прохода мы оказываемся на уровень выше и в правом углу
        И теперь идем в левый угол

        '''


        while angle_now != CONST_ANGLE_START: # стартуем  
            client_socket.sendall(Photo().encode()) # еще одну улыбочку:) 
            response = client_socket.recv(1024).decode() # принимаем наше личико:)

            if CheckResponse(response) != "OK": # все ли ок? Если нет, то ломает этот аппарат 
                break

            print(response) # если ок, то смотрим на красавичка 
            time.sleep(1)  # Немного замерзаем от такой красоты 

            client_socket.sendall(Left_step(angle_now - defaul_step).encode()) # теперь едем влево
            response = client_socket.recv(1024).decode() # принимаем ответ 

            if CheckResponse(response) != "OK": # если не ок, тогда ломаем циклу лицо:)
                break
            else:
                angle_now -= defaul_step # иначе обновляем значение угла

            print(response)    
            time.sleep(1)  # Добавляем задержку в 1 секунду
        
        if response != "OK": # если мы в цикле выше получили не ок, то вылетаем  
            break
        
        height_now += 1 # тут пока что затычка, потом допишу 
finally:
    # Закрытие соединения
    client_socket.close()
    server_socket.close()
