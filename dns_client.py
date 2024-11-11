import socket

def main():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the DNS server
    client_socket.connect(("127.0.0.1", 12345))

    # Get the domain name from the user
    domain_name = input("Enter domain name: ")

    # Send the domain name to the server
    client_socket.send(domain_name.encode("utf-8"))

    # Receive the IP address from the server
    ip_address = client_socket.recv(1024).decode("utf-8")
    print(f"IP Address: {ip_address}")

    client_socket.close()

if __name__ == "__main__":
    main()
