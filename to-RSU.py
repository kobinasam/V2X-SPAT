import socket
import time

# Define the RSU's IP address and port
RSU_IP = '192.168.10.17'
RSU_PORT = 1516

# Open the file for reading
with open("decoded_message.txt", "r") as file:
    packet = b""  # Variable to store the current packet
    in_packet = False  # Flag to indicate if currently inside a packet
    ignore_content = False  # Flag to indicate if content should be ignored

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Iterate over each line in the file
    for line in file:
        # Check if the line contains "ERROR", "Error", or "error"
        if "ERROR" in line.upper():
            ignore_content = True
            continue  # Skip this line

        # Check if the line starts with "0013"
        if line.startswith("0013"):
            # If currently inside a packet, send it
            if in_packet:
                sock.sendto(packet, (RSU_IP, RSU_PORT))
                time.sleep(0.1)  # Delay 100 milliseconds
            # Start a new packet
            packet = line.encode()  # Encode the line as bytes
            in_packet = True
            ignore_content = False  # Reset the ignore flag
        # Check if the line starts with "0014"
        elif line.startswith("0014"):
            # If currently inside a packet or ignoring content, continue
            if in_packet or ignore_content:
                continue
        else:
            # If currently inside a packet and not ignoring content, append the line to the packet
            if in_packet and not ignore_content:
                packet += line.encode()  # Encode the line as bytes
                # Check if the line is empty or starts with "0013" or "0014",
                # indicating the end of the packet
                if line.strip() == "" or line.startswith("0013") or line.startswith("0014"):
                    in_packet = False  # Reset the flag
    # Send the last packet if it wasn't sent inside the loop
    if in_packet:
        sock.sendto(packet, (RSU_IP, RSU_PORT))
