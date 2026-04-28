import socket

# --- NETWORK SCANNER UTILITY ---

def validate_port(port_str):
    """Validates that the given port is an integer between 1 and 65535."""
    try:
        port = int(port_str)
        if 1 <= port <= 65535:
            return port
        return None
    except ValueError:
        return None

def scan_target(ip_address, start_port, end_port):
    """Scans a range of ports on a target IP address using the socket library."""
    open_ports = []
    print(f"\n[!] Starting scan on {ip_address} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) 
        
        try:
            result = s.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
        except socket.error as e:
            print(f"Socket error attempting to connect to port {port}: {e}")
        finally:
            s.close()
            
    return open_ports

def run_port_scanner_utility():
    """Main interface function for the Network Scanner utility."""
    print("\n" + "="*40)
    print("       NETWORK PORT SCANNER")
    print("="*40)
    
    target_ip = input("Enter target IP to scan (e.g., 127.0.0.1): ").strip()
    if not target_ip:
        print("[-] Invalid IP address. Returning to menu.")
        return

    start_port_input = input("Enter start port [1]: ").strip() or "1"
    end_port_input = input("Enter end port [1024]: ").strip() or "1024"

    start_port = validate_port(start_port_input)
    end_port = validate_port(end_port_input)

    if start_port is None or end_port is None or start_port > end_port:
        print("[-] Error: Ports must be numbers between 1 and 65535, and start must be less than or equal to end.")
        return

    try:
        open_ports = scan_target(target_ip, start_port, end_port)
        print("\n[+] Scan Complete.")
        if open_ports:
            print(f"Open ports found on {target_ip}:")
            for p in open_ports:
                print(f"  - Port {p} is OPEN")
        else:
            print(f"No open ports found on {target_ip} in range {start_port}-{end_port}.")
    except Exception as e:
        print(f"[-] An unexpected error occurred during the scan: {e}")