import socket

# Define a dictionary to simulate the DNS records
dns_records = {
    "mjcet.it.edu": "192.100.100.6",
    "example.txt": "93.184.216.34",
    "google.com": "142.250.182.78"
}

def handle_client(client_socket):
    # Receive the domain name from the client
    domain_name = client_socket.recv(1024).decode("utf-8")
    print(f"Received request for domain: {domain_name}")

    # Look up the IP address in the DNS records
    ip_address = dns_records.get(domain_name, "Domain not found")

    # Send the IP address back to the client
    client_socket.send(ip_address.encode("utf-8"))

    client_socket.close()

def main():
    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("DNS Server started and waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
