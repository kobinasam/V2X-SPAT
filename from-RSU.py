import socket

# Define the port to listen on
LISTEN_PORT = 1516

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('0.0.0.0', LISTEN_PORT))

print(f"Listening for messages on port {LISTEN_PORT}...")

# Infinite loop to continuously receive messages
while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)  # Adjust buffer size as needed

    # Decode the received data
    decoded_data = data.decode()

    # Print the received message and its source address
    print(f"Received message from {addr}:")
    print(decoded_data)
