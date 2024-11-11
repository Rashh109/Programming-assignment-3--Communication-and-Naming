import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 12346  # Changed port number to 12346

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    file_name = input("Enter the file name to download: ")
    client_socket.send(file_name.encode("utf-8"))

    file_content = client_socket.recv(1024 * 1024)
    if file_content == b"File not found":
        print("Error: File not found on server")
    else:
        with open(f"downloaded_{file_name}", "wb") as file:
            file.write(file_content)
        print(f"File {file_name} downloaded successfully")

    client_socket.close()

if __name__ == "__main__":
    main()
