import socket


def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', 6379))
        client_socket.sendall(command.encode('utf-8'))
        response = client_socket.recv(4096)
    return response.decode('utf-8')


def main():
    print("Redis Client")
    print("Enter Redis commands (type 'exit' to quit):")

    while True:
        cmd = input(">> ")
        if cmd.lower() == 'exit':
            break
        response = send_command(cmd)
        print(response)


if __name__ == '__main__':
    main()