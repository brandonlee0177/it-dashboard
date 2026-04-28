"""
IT Dashboard - Network & System Management Tool
Course: KU_JAX_COP1034CD4-104062026
Assignment: Week 3 - OOP & Network Topology
"""

from datetime import datetime
import logging
import os
import subprocess
import turtle
import random
import socket  # Added for Network Scanner utility

# --- 1. BOILERPLATE & CONSTANTS ---
debug = False
logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)

APPNAME = "IT Dashboard"
VERSION = "0.5.0"
AUTHOR = "Brandon Lee"
COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
COURSE_NAME = "Programming for Technology Professionals - KU_JAX_COP1034CD4-104062026"
INSTRUCTORS_NAME = "Professor Mora"
ASSIGNMENT_NAME = "Week 3 - OOP Network Management"

# --- 2. CLASS DEFINITIONS (OOP CORE) ---

class NetworkDevice:
    """Base class representing a generic network device."""
    
    def __init__(self, hostname, ip_address, device_type, status="online"):
        """
        Initialize a NetworkDevice with identity and status fields.
        
        Args:
            hostname (str): Unique name of the device.
            ip_address (str): IPv4 address.
            device_type (str): Category (router, switch, server).
            status (str): Operational status.
        """
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.status = status

    def __str__(self):
        """Return a one-line summary string for this device."""
        return f"[{self.device_type.upper()}] {self.hostname} | {self.ip_address} | Status: {self.status}"

    def ping(self):
        """Simulate a ping to this device and return a result string."""
        return f"Reply from {self.ip_address}: bytes=32 time=2ms TTL=128"

    def get_info(self):
        """Return a formatted string with this device's details."""
        return str(self)

class Router(NetworkDevice):
    """A network router. Extends NetworkDevice with routing information."""
    
    def __init__(self, hostname, ip_address, routing_protocol="OSPF"):
        """Initialize a Router — calls super().__init__."""
        super().__init__(hostname, ip_address, device_type="router")
        self.routing_protocol = routing_protocol
        self.routes = ["10.0.0.0/8", "172.16.0.0/12", "192.168.1.0/24"]

    def get_info(self):
        """Override base get_info to include routing protocol and routes."""
        base_info = super().get_info()
        route_data = f"\n  Protocol : {self.routing_protocol}\n  Routes   : {', '.join(self.routes)}"
        return base_info + route_data

    def show_routes(self):
        """Return the current simulated routing table."""
        return self.routes

class Switch(NetworkDevice):
    """A network switch. Extends NetworkDevice with VLAN and port information."""
    
    def __init__(self, hostname, ip_address, port_count=24):
        """Initialize a Switch — calls super().__init__."""
        super().__init__(hostname, ip_address, device_type="switch")
        self.port_count = port_count
        self.vlans = ["VLAN 1 (default)", "VLAN 10 (Sales)", "VLAN 20 (HR)"]

    def get_info(self):
        """Override base get_info to include port count and VLAN list."""
        base_info = super().get_info()
        vlan_data = f"\n  Ports    : {self.port_count}\n  VLANs    : {', '.join(self.vlans)}"
        return base_info + vlan_data

class DeviceManager:
    """Manages a collection of NetworkDevice objects."""
    
    def __init__(self):
        """Initialize with an empty device list."""
        self.devices = []

    def add_device(self, device):
        """Add a NetworkDevice (or subclass) to the devices list."""
        self.devices.append(device)
        print(f"Added: {device.hostname}")

    def remove_device(self, hostname):
        """Remove the device with the given hostname. Print error if not found."""
        for d in self.devices:
            if d.hostname.upper() == hostname.upper():
                self.devices.remove(d)
                print(f"SUCCESS: {hostname} has been decommissioned.")
                return
        print(f"ERROR: Device '{hostname}' not found in inventory.")

    def find_device(self, hostname):
        """Return the device object matching hostname, or None if not found."""
        for d in self.devices:
            if d.hostname.upper() == hostname.upper():
                return d
        return None

    def list_all(self):
        """Demonstrate polymorphism by calling get_info() on mixed device types."""
        if not self.devices:
            print("\nInventory is currently empty.")
            return
        print("\n" + "="*40)
        print("       NETWORK DEVICE INVENTORY")
        print("="*40)
        for device in self.devices:
            print(device.get_info())
            print("-" * 40)

# --- 3. SYSTEM FUNCTIONS (LEGACY CORE) ---

def print_header():
    """Prints the project branding and author metadata."""
    print("--------------------------------------------------")
    print(f"Author     : {AUTHOR}")
    print(f"Copyright  : {COPYRIGHT}")
    print("--------------------------------------------------")
    print(f"Course     : {COURSE_NAME}")
    print(f"Instructor : {INSTRUCTORS_NAME}")
    print(f"Assignment : {ASSIGNMENT_NAME}")
    print("--------------------------------------------------")
    print(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("--------------------------------------------------")

def run_system_checks():
    """Simulates real-time system health checks via loop iteration."""
    checks = ["CPU Usage", "Memory Usage", "Disk Space", "Network Connectivity", "Firewall Status"]
    print("\n[!] Running System Integrity Checks...")
    for check in checks:
        print(f"  - {check:<22}: [ PASS ]")
    print("[+] All system checks completed successfully.")

def print_report(server_name, ip, dept, total, used, usage_pct, status):
    """
    Displays the high-detail IT System Status Report.
    This preserves the formatted reporting from Week 1 & 2.
    """
    free_disk_gb = total - used
    print("\n" + "="*40)
    print("        IT SYSTEM STATUS REPORT")
    print("="*40)
    print(f"{'Server Name':<15}: {server_name}")
    print(f"{'IP Address':<15}: {ip}")
    print(f"{'Department':<15}: {dept}")
    print("-" * 40)
    print(f"{'Total Disk':<15}: {total} GB")
    print(f"{'Used Disk':<15}: {used} GB")
    print(f"{'Free Disk':<15}: {free_disk_gb} GB")
    print(f"{'Usage':<15}: {usage_pct:.2f}%")
    print(f"{'Status':<15}: {status}")
    print("="*40)

def analyzeserverlogs():
    """
    Parses 'server.log' and generates 'logssummary.txt'.
    Preserves log parsing, severity counting, and notepad integration.
    """
    print("\n--- Initializing Log Analysis Engine ---")
    
    severitycounts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
    uniqueerrors = set()
    criticalevents = set()
    linesread = 0

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGPATH = os.path.join(SCRIPT_DIR, "server.log")

    if not os.path.exists(LOGPATH):
        print(f"Error: server.log not found. Place it at: {LOGPATH}")
        return

    try:
        with open(LOGPATH, "r") as f:
            for line in f:
                linesread += 1
                parts = line.strip().split(maxsplit=3)
                
                if len(parts) < 3:
                    continue

                # Severity extraction logic
                severity = None
                message = None

                if parts[2].startswith("[") and "]" in parts[2]:
                    end = parts[2].find("]")
                    severity = parts[2][1:end].upper()
                    message = parts[3] if len(parts) > 3 else "No message"
                
                if severity in severitycounts:
                    severitycounts[severity] += 1
                    if severity == "ERROR":
                        uniqueerrors.add(message)
                    if severity == "CRITICAL":
                        criticalevents.add(message)

        # Calculate metrics
        totalseen = sum(severitycounts.values())
        errorrate = (severitycounts["ERROR"] / totalseen * 100) if totalseen > 0 else 0.0

        SUMMARY_PATH = os.path.join(SCRIPT_DIR, "logssummary.txt")
        with open(SUMMARY_PATH, "w") as out:
            out.write("==================================\n")
            out.write("      SERVER LOG ANALYSIS REPORT  \n")
            out.write("==================================\n")
            out.write(f"Timestamp    : {datetime.now()}\n")
            out.write(f"Log Path     : {LOGPATH}\n")
            out.write(f"Lines Processed: {linesread}\n")
            out.write("----------------------------------\n")
            out.write("Severity Counts:\n")
            for level, count in severitycounts.items():
                out.write(f"  {level:<10}: {count}\n")
            out.write("----------------------------------\n")
            out.write(f"Calculated Error Rate: {errorrate:.2f}%\n")
            out.write("----------------------------------\n")
            out.write(f"UNIQUE ERRORS FOUND ({len(uniqueerrors)}):\n")
            for err in sorted(uniqueerrors):
                out.write(f"  - {err}\n")
            out.write(f"CRITICAL EVENTS FOUND ({len(criticalevents)}):\n")
            for crit in sorted(criticalevents):
                out.write(f"  - {crit}\n")
            out.write("==================================\n")

        print(f"Analysis Complete! Summary saved to: {SUMMARY_PATH}")
        
        # Open in Notepad automatically
        subprocess.Popen(['notepad.exe', SUMMARY_PATH])

    except Exception as e:
        print(f"An unexpected error occurred during analysis: {e}")

# --- 4. GRAPHICS FUNCTIONS ---

def draw_topology(manager):
    """
    Uses Turtle Graphics to draw a topology map based on the DeviceManager list.
    """
    if not manager.devices:
        print("\n[!] No devices to draw. Please add a Router or Switch first.")
        return
    
    print("\n[+] Launching Turtle Graphics Topology...")
    screen = turtle.Screen()
    screen.title("Live Network Topology - IT Dashboard")
    screen.bgcolor("#0a0e1a")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    x_start = -300
    x_gap = 150
    
    for i, device in enumerate(manager.devices):
        x = x_start + (i * x_gap)
        
        t.penup()
        t.goto(x, 0)
        t.pendown()

        # Polymorphic Color Selection
        if device.device_type == "router":
            t.fillcolor("#10b981") # Green
        else:
            t.fillcolor("#3b82f6") # Blue

        # Draw box
        t.begin_fill()
        for _ in range(2):
            t.forward(80)
            t.left(90)
            t.forward(50)
            t.left(90)
        t.end_fill()

        # Label device
        t.penup()
        t.goto(x + 40, -25)
        t.color("white")
        t.write(device.hostname, align="center", font=("Arial", 10, "bold"))
        
        t.goto(x + 40, -40)
        t.write(device.ip_address, align="center", font=("Arial", 8, "normal"))

    print("--- Close Turtle window to return to Main Menu ---")
    turtle.done()

# --- 5. NETWORK SCANNER UTILITY (NEW ADDITION) ---

def validate_port(port_str):
    """
    Validates that the given port is an integer between 1 and 65535.
    Returns the port as an int if valid, otherwise returns None.
    """
    try:
        port = int(port_str)
        if 1 <= port <= 65535:
            return port
        return None
    except ValueError:
        return None

def scan_target(ip_address, start_port, end_port):
    """
    Scans a range of ports on a target IP address using the socket library.
    Catches realistic connection errors and returns a list of open ports.
    """
    open_ports = []
    print(f"\n[!] Starting scan on {ip_address} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        # Create a socket object for each port check
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) 
        
        try:
            # connect_ex returns 0 if the connection succeeds (port is open)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
        except socket.error as e:
            # Inline comment: catch specific networking errors without crashing
            print(f"Socket error attempting to connect to port {port}: {e}")
        finally:
            s.close()
            
    return open_ports

def run_port_scanner_utility():
    """Main interface function for the Network Scanner utility."""
    print("\n" + "="*40)
    print("       NETWORK PORT SCANNER")
    print("="*40)
    
    # Input validation on user-supplied data
    target_ip = input("Enter target IP to scan (e.g., 127.0.0.1): ").strip()
    if not target_ip:
        print("[-] Invalid IP address. Returning to menu.")
        return

    start_port_input = input("Enter start port [1]: ").strip() or "1"
    end_port_input = input("Enter end port [1024]: ").strip() or "1024"

    start_port = validate_port(start_port_input)
    end_port = validate_port(end_port_input)

    # Conditionals making a real decision based on boundary constraints
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

# --- 6. MAIN LOGIC AND MENU ---

def main():
    """Entry point for the IT Dashboard application."""
    print_header()
    
    # Initialize OOP Manager
    manager = DeviceManager()
    
    # Initialize Legacy Variables
    server_name = "Layla"
    ip_address = "10.0.0.1"
    department = "New to IT"
    total_disk_gb = 70
    used_disk_gb = 30
    usage_pct = 42.86
    disk_status = "OK - Disk usage is normal"
    report_ready = True

    while True:
        print("\n" + "*"*32)
        print(f"   {APPNAME} v{VERSION} MAIN MENU")
        print("*"*32)
        print("1) Manage Network Devices (Add Router/Switch)")
        print("2) List Device Inventory (Polymorphism)")
        print("3) Remove Device by Hostname")
        print("4) View Legacy System Status Report")
        print("5) Configure System Report Settings")
        print("6) Run Live System Health Checks")
        print("7) Analyze Server Logs & Metrics")
        print("8) Draw Network Topology (Turtle)")
        print("9) Ping a Device")
        print("10) Run Network Port Scanner Utility")  # Added Scanner Option
        print("0) Exit Dashboard")
        print("*"*32)

        choice = input("Enter selection: ").strip()

        if choice == "1":
            dtype = input("Add (R)outer or (S)witch? ").strip().upper()
            hname = input("Enter Hostname: ").strip()
            ipaddr = input("Enter IP Address: ").strip()
            
            if dtype == 'R':
                proto = input("Enter Routing Protocol [OSPF]: ") or "OSPF"
                manager.add_device(Router(hname, ipaddr, proto))
            elif dtype == 'S':
                ports = input("Enter Port Count [24]: ") or "24"
                manager.add_device(Switch(hname, ipaddr, int(ports)))
            else:
                print("Invalid device type selection.")

        elif choice == "2":
            manager.list_all()

        elif choice == "3":
            hname = input("Enter Hostname to remove: ")
            manager.remove_device(hname)

        elif choice == "4":
            if report_ready:
                print_report(server_name, ip_address, department, 
                             total_disk_gb, used_disk_gb, usage_pct, disk_status)
            else:
                print("Report not configured. Use Option 5 first.")

        elif choice == "5":
            server_name = input(f"Server Name [{server_name}]: ") or server_name
            ip_address = input(f"IP Address [{ip_address}]: ") or ip_address
            department = input(f"Department [{department}]: ") or department
            try:
                total_disk_gb = int(input(f"Total Disk [{total_disk_gb}]: ") or total_disk_gb)
                used_disk_gb = int(input(f"Used Disk [{used_disk_gb}]: ") or used_disk_gb)
                
                # Re-calculate usage
                usage_pct = (used_disk_gb / total_disk_gb) * 100
                if usage_pct > 90: disk_status = "CRITICAL"
                elif usage_pct > 75: disk_status = "WARNING"
                else: disk_status = "OK"
                report_ready = True
                print("[+] Report settings updated.")
            except ValueError:
                print("Invalid numeric entry for disk space.")

        elif choice == "6":
            run_system_checks()

        elif choice == "7":
            analyzeserverlogs()

        elif choice == "8":
            draw_topology(manager)

        elif choice == "9":
            hname = input("Hostname to ping: ")
            dev = manager.find_device(hname)
            if dev:
                print(dev.ping())
            else:
                print("Device not found in inventory.")

        elif choice == "10":
            run_port_scanner_utility()

        elif choice == "0":
            print("\nShutting down Dashboard...")
            print("Smell ya later stinky.")
            break
        
        else:
            print("Selection invalid. Please try again.")

if __name__ == "__main__":
    main()