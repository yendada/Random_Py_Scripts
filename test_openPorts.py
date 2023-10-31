#Checking Port scanning based on user input


import socket

host = input("Enter the host to scan (e.g., example.com): ")
port = int(input("Enter the port to check (e.g., 80): "))  # Add the missing closing parenthesis

def port_scan(host, port):
    try:
        # Attempt to create a socket to the specified host and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} on {host} is open.")
            else:
                print(f"Port {port} on {host} is closed.")
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to the server.")

port_scan(host, port)



