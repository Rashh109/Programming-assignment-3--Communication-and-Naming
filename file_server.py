import socket

def handle_client(client_socket):
    file_name = client_socket.recv(1024).decode("utf-8")
    print(f"Received request for file: {file_name}")
    try:
        with open(file_name, "rb") as file:
            file_content = file.read()
            client_socket.send(file_content)
    except FileNotFoundError:
        client_socket.send(b"File not found")

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12346))  # Changed port number to 12346
    server_socket.listen(5)
    print("File Server started and waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
