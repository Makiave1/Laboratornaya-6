#Лабораторная работа №6
#Жидков А. В.
#ДПИ22-1
#UDP-Сервер
import socket
import threading

class UDPChatServer:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = set()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        print("Сервер запущен. Ожидание сообщений...")

        try:
            while True:
                data, addr = self.server_socket.recvfrom(1024)
                message = data.decode()
                print(f"Получено сообщение от {addr}: {message}")

                if addr not in self.clients:
                    self.clients.add(addr)

                # Рассылка сообщения всем клиентам
                self.broadcast(message, addr)
        except KeyboardInterrupt:
            print("Остановка сервера.")
        finally:
            self.server_socket.close()

    def broadcast(self, message, sender_addr):
        for client in self.clients:
            if client != sender_addr:
                self.server_socket.sendto(message.encode(), client)

if __name__ == "__main__":
    server = UDPChatServer()
    server.start()