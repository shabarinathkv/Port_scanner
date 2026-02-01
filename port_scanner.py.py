import socket

try:
    # Ask the user for target IP address or hostname
    target = input("Enter the target IP address or hostname: ")

    # Define the range of ports to scan (1–1024 are well-known ports)
    ports = range(1, 1025)

    # Common ports and their associated services
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "TELNET",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "NETBIOS",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MYSQL",
        8080: "HTTP-ALT"
    }

    # Scan each port in the defined range
    for port in ports:
        # Create a new socket for each port
        s = socket.socket()
        
        # Set timeout to avoid long waiting
        s.settimeout(0.2)

        # Try to connect to the target on the current port
        result = s.connect_ex((target, port))

        # If result is 0, the port is open
        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[+] Port {port} ({service}) is OPEN")
        else:
            print(f"[-] Port {port} is closed")

        # Close the socket connection
        s.close()

except socket.gaierror:
    print("Invalid hostname or IP address")

except KeyboardInterrupt:
    print("\nScan stopped by user")

except Exception as e:
    print(f"An error occurred: {e}")
