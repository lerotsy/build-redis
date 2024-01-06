import socket
import threading

EOR = "\r\n"  # End of Response


class RedisServer:
    def __init__(self, host='127.0.0.1', port=6379):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.data_store = {}

    def listen(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client,
                             args=[client_socket]).start()

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(1024).decode('utf-8').strip()
            if request:
                response = self.process_request(request)
                client_socket.send(response.encode('utf-8'))
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"Error: {e}")

        client_socket.close()

    def process_request(self, request):
        parts = request.split()
        command = parts[0].upper()

        if command == 'PING':
            response = '+PONG'
        elif command == 'ECHO':
            response = " ".join(parts[1:])
        elif command == 'SET':
            self.data_store[parts[1]] = parts[2]
            return "+OK"
        elif command == 'GET':
            response = self.data_store.get(parts[1], '(nil)')
        else:
            response = '-ERR Unknown Commnad'
        return f"{response}{EOR}"


