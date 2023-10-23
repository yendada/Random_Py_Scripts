import socket

# Define the target host and a list of ports to check
# example.com or any similar website
# Only to be used with proper authorization

target_host = "example.com"
target_ports = [80, 443, 8080, 22, 21]

# Function to check if a port is open
def is_port_open(host, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Set a timeout for the connection attempt
            s.settimeout(2)
            # Try to connect to the host and port
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

# Check if the ports are open
for port in target_ports:
    if is_port_open(target_host, port):
        print(f"Port {port} is open on {target_host}")
    else:
        print(f"Port {port} is closed on {target_host}")
