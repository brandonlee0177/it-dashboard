import json
import os

# --- CLASS DEFINITIONS (OOP CORE) ---

class NetworkDevice:
    """Base class representing a generic network device."""
    def __init__(self, hostname, ip_address, device_type, status="online"):
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.status = status

    def __str__(self):
        return f"[{self.device_type.upper()}] {self.hostname} | {self.ip_address} | Status: {self.status}"

    def ping(self):
        return f"Reply from {self.ip_address}: bytes=32 time=2ms TTL=128"

    def get_info(self):
        return str(self)

class Router(NetworkDevice):
    """A network router. Extends NetworkDevice with routing information."""
    def __init__(self, hostname, ip_address, routing_protocol="OSPF"):
        super().__init__(hostname, ip_address, device_type="router")
        self.routing_protocol = routing_protocol
        self.routes = ["10.0.0.0/8", "172.16.0.0/12", "192.168.1.0/24"]

    def get_info(self):
        base_info = super().get_info()
        route_data = f"\n  Protocol : {self.routing_protocol}\n  Routes   : {', '.join(self.routes)}"
        return base_info + route_data

    def show_routes(self):
        return self.routes

class Switch(NetworkDevice):
    """A network switch. Extends NetworkDevice with VLAN and port information."""
    def __init__(self, hostname, ip_address, port_count=24):
        super().__init__(hostname, ip_address, device_type="switch")
        self.port_count = port_count
        self.vlans = ["VLAN 1 (default)", "VLAN 10 (Sales)", "VLAN 20 (HR)"]

    def get_info(self):
        base_info = super().get_info()
        vlan_data = f"\n  Ports    : {self.port_count}\n  VLANs    : {', '.join(self.vlans)}"
        return base_info + vlan_data

class DeviceManager:
    """Manages a collection of NetworkDevice objects and handles data persistence."""
    
    def __init__(self, filename="devices.json"):
        """Initialize and automatically load saved devices."""
        self.devices = []
        self.filename = filename
        self.load_devices() # Load from file on startup

    def add_device(self, device):
        self.devices.append(device)
        print(f"[+] Added: {device.hostname}")
        self.save_devices() # Save immediately after adding

    def remove_device(self, hostname):
        for d in self.devices:
            if d.hostname.upper() == hostname.upper():
                self.devices.remove(d)
                print(f"[+] SUCCESS: {hostname} has been decommissioned.")
                self.save_devices() # Save immediately after removing
                return
        print(f"[-] ERROR: Device '{hostname}' not found in inventory.")

    def find_device(self, hostname):
        for d in self.devices:
            if d.hostname.upper() == hostname.upper():
                return d
        return None

    def list_all(self):
        if not self.devices:
            print("\nInventory is currently empty.")
            return
        print("\n" + "="*40)
        print("       NETWORK DEVICE INVENTORY")
        print("="*40)
        for device in self.devices:
            print(device.get_info())
            print("-" * 40)

    # --- DATA PERSISTENCE METHODS ---

    def save_devices(self):
        """Serializes the device objects to a JSON file."""
        with open(self.filename, 'w') as f:
            json_data = []
            for d in self.devices:
                # __dict__ easily grabs all the object's variables (hostname, ip, etc.)
                json_data.append(d.__dict__)
            json.dump(json_data, f, indent=4)

    def load_devices(self):
        """Loads devices from a JSON file and reconstructs the OOP objects."""
        if not os.path.exists(self.filename):
            return # If the file doesn't exist yet, just start with an empty list

        try:
            with open(self.filename, 'r') as f:
                json_data = json.load(f)
                self.devices = [] # Clear the list before loading
                
                for item in json_data:
                    # Reconstruct the correct object type based on the saved data
                    if item.get("device_type") == "router":
                        r = Router(item["hostname"], item["ip_address"], item.get("routing_protocol", "OSPF"))
                        r.status = item.get("status", "online")
                        self.devices.append(r)
                    elif item.get("device_type") == "switch":
                        s = Switch(item["hostname"], item["ip_address"], item.get("port_count", 24))
                        s.status = item.get("status", "online")
                        self.devices.append(s)
            print(f"[!] Loaded {len(self.devices)} devices from {self.filename}.")
        except Exception as e:
            print(f"[-] Error loading memory file: {e}")