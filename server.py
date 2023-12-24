import socket

def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.0.143"
    port = 12345

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Эхо-сервер запущен на {host}:{port}...")

        while True:
            client_socket, addr = server_socket.accept()
            print(f"Подключено от {addr}")

            try:
                data = client_socket.recv(1024)
                while data:
                    print(f"Получено: {data.decode()}")
                    client_socket.send(data)
                    data = client_socket.recv(1024)

                print("Подключение закрыто")
            except Exception as e:
                print(f"Ошибка при обработке подключения: {e}")
            finally:
                client_socket.close()

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    echo_server()
