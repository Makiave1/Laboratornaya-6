#Лабораторная работа №6
#Жидков А. В.
#ДПИ22-1
#UDP-Клиент
import socket
import threading

class UDPChatClient:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Запускаем поток для приема сообщений
        threading.Thread(target=self.receive_messages, daemon=True).start()

        print("Соединение с сервером установлено.")
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            self.client_socket.sendto(message.encode(), (self.host, self.port))

        self.client_socket.close()
        print("Разрыв соединения с сервером.")

    def receive_messages(self):
        while True:
            try:
                data, _ = self.client_socket.recvfrom(1024)
                print(f"\nНовое сообщение: {data.decode()}")
            except OSError:
                break

if __name__ == "__main__":
    client = UDPChatClient()
    client.start()
