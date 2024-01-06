import socket

EOR = "\r\n"  # End of Response
class RedisServer:
    def __init__(self, host='127.0.0.1', port=6379):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.data_store = {}

    def listen(self):
        client_socket, addr = self.server_socket.accept()
        print(f"Connection from {addr}")
        self.handle_client(client_socket)

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
            response = ''
        else:
            response = '-ERR Unknown Commnad'
        response = '+PONG'
        return f"{response}{EOR}"


