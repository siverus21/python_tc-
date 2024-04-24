import socket
import errno 
import serial
import time

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()

def initialize_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.31.52', 9090)
    client_socket.connect(server_address)
    return client_socket

def receive_command(client_socket):
    try:
        command = client_socket.recv(1024).decode()
        print("Получена команда от сервера:", command)
        return command
    except socket.error as e:
        if e.errno == errno.EPIPE:
            print("Соединение было разорвано")
            # return f"u {TH}"

def send_response(client_socket, response):
    try:
        client_socket.sendall(response.encode())
    except socket.error as e:
        if e.errno == errno.EPIPE:
            print("Соединение было разорвано")

def close_connection(client_socket):
    client_socket.close()


def run_client():
    client_socket = initialize_client()
    ports = serial.tools.list_ports.comports()
    newPort = 0
    for port in ports:
        newPort = port.device

    ser = serial.Serial(newPort, 115200)

    try:
        while True:
            try:
                command = receive_command(client_socket)
                ser.write(command.encode('utf-8'))
                time.sleep(4)
                response = ser.readline()
                response = response.decode('utf-8')
                print(response)
                if(response != "1"):
                    ser.close()
                    close_connection(client_socket)
                # if command == "END":
                #     print("Получена команда завершения от сервера.")
                #     break

                # if command != "photo":
                #     command_parts = command.split(",")
                #     action = command_parts[0]
                #     try:
                #         value = int(command_parts[1])
                #     except:
                #         response = "Указанное значение не является числом!"

                #     if action in commands:
                #         response = "OK"
                #     else:
                #         response = "Неверная команда"
                # elif command == "photo":
                #     response = "OK"
            except:
                response = 'error'
            send_response(client_socket, response)
    finally:
        ser.close()
        close_connection(client_socket)

run_client()
