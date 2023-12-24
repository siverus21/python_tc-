import socket

def send_data(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.143"  # Замените на IP-адрес вашего сервера
    port = 12345

    try:
        client_socket.connect((host, port))
        client_socket.send(message.encode())

        data = client_socket.recv(1024)
        print(f"Получено от сервера: {data.decode()}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    message = "Привет, сервер! Это сообщение от клиента."
    send_data(message)
