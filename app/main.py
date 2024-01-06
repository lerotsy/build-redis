from .redis_server import RedisServer


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = RedisServer(host='localhost', port=6379)
    server.listen()

    # server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept()


if __name__ == "__main__":
    main()
