import tkinter as tk
from tkinter import scrolledtext, simpledialog
from tkinter import messagebox
import sys
from datetime import datetime

# Import your existing custom modules
from config import APPNAME, VERSION, AUTHOR
from network_devices import DeviceManager, Router, Switch
from system_utils import run_system_checks, print_report, analyzeserverlogs
from graphics import draw_topology
from network_scanner import scan_target, validate_port

class PrintRedirector:
    """Catches standard print() statements and redirects them to a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END) # Auto-scroll to the bottom

    def flush(self):
        pass # Required for file-like objects, but we don't need to do anything

class DashboardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{APPNAME} v{VERSION} - Admin Console")
        self.root.geometry("950x650")
        
        def confirm_exit(self):
         """Spawns a popup to confirm before closing the application."""
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to shut down the Dashboard?"):
            print("\nShutting down Dashboard...")
            self.root.quit()
        
        # Dark / Tech Aesthetic Colors
        self.bg_color = "#0a0e1a"       # Deep dark blue/black
        self.text_color = "#00ffcc"     # Cyan/Neon Green text
        self.btn_bg = "#1f2937"         # Dark gray buttons
        self.btn_fg = "#ffffff"         # White button text
        
        self.root.configure(bg=self.bg_color)

        # Dashboard State Variables
        self.manager = DeviceManager()
        self.author = AUTHOR
        self.server_name = "Layla"
        self.ip_address = "10.0.0.1"
        self.department = "New to IT"
        self.total_disk_gb = 70
        self.used_disk_gb = 30
        self.usage_pct = 42.86
        self.disk_status = "OK - Disk usage is normal"
        self.report_ready = True

        self.setup_ui()

        # Redirect standard output to our text box
        sys.stdout = PrintRedirector(self.console_output)
        
        print(f"--- Welcome to {APPNAME} v{VERSION} ---")
        print(f"System Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Ready for input...\n")

    def setup_ui(self):
        """Builds the buttons and the output terminal screen."""
        # Left Panel for Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color, width=250)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Right Panel for Output
        output_frame = tk.Frame(self.root, bg=self.bg_color)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Output Terminal
        self.console_output = scrolledtext.ScrolledText(
            output_frame, 
            bg="#000000", 
            fg=self.text_color, 
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.console_output.pack(fill=tk.BOTH, expand=True)

        # Define Buttons
        buttons = [
            ("1. Add Network Device", self.add_device),
            ("2. List Device Inventory", self.list_devices),
            ("3. Remove Device", self.remove_device),
            ("4. View System Report", self.view_report),
            ("5. Configure Report", self.config_report),
            ("6. Run Health Checks", self.run_health_checks),
            ("7. Analyze Server Logs", self.analyze_logs),
            ("8. Draw Network Topology", self.draw_network),
            ("9. Ping Device", self.ping_device),
            ("10. Port Scanner Utility", self.run_scanner),
            ("0. Clear Screen", self.clear_screen),
            ("Exit", self.confirm_exit)
        ]

        # Generate Buttons dynamically
        for text, command in buttons:
            btn = tk.Button(
                button_frame, 
                text=text, 
                command=command, 
                bg=self.btn_bg, 
                fg=self.btn_fg, 
                font=("Arial", 10, "bold"),
                relief=tk.FLAT,
                width=25,
                pady=5
            )
            btn.pack(pady=5)

    # --- BUTTON ACTION METHODS ---

    def clear_screen(self):
        """Clears the text terminal."""
        self.console_output.delete(1.0, tk.END)

    def add_device(self):
        dtype = simpledialog.askstring("Device Type", "Add (R)outer or (S)witch?", parent=self.root)
        if not dtype:
            return
        dtype = dtype.strip().upper()
        
        hname = simpledialog.askstring("Hostname", "Enter Hostname:", parent=self.root)
        if not hname:
            return
        
        ipaddr = simpledialog.askstring("IP Address", "Enter IP Address:", parent=self.root)
        if not ipaddr:
            return

        if dtype == 'R':
            proto = simpledialog.askstring("Protocol", "Enter Routing Protocol (e.g., OSPF):", parent=self.root) or "OSPF"
            self.manager.add_device(Router(hname, ipaddr, proto))
        elif dtype == 'S':
            ports = simpledialog.askinteger("Ports", "Enter Port Count:", initialvalue=24, parent=self.root) or 24
            self.manager.add_device(Switch(hname, ipaddr, ports))
        else:
            print("[-] Invalid device type selection.")

    def list_devices(self):
        self.manager.list_all()

    def remove_device(self):
        hname = simpledialog.askstring("Remove Device", "Enter Hostname to remove:", parent=self.root)
        if hname:
            self.manager.remove_device(hname)

    def view_report(self):
        if self.report_ready:
            print_report(self.server_name, self.ip_address, self.department, 
                         self.total_disk_gb, self.used_disk_gb, self.usage_pct, self.disk_status)
        else:
            print("[-] Report not configured. Configure settings first.")

    def config_report(self):
        self.server_name = simpledialog.askstring("Config", "Server Name:", initialvalue=self.server_name) or self.server_name
        self.ip_address = simpledialog.askstring("Config", "IP Address:", initialvalue=self.ip_address) or self.ip_address
        self.department = simpledialog.askstring("Config", "Department:", initialvalue=self.department) or self.department
        
        try:
            total = simpledialog.askinteger("Config", "Total Disk GB:", initialvalue=self.total_disk_gb)
            used = simpledialog.askinteger("Config", "Used Disk GB:", initialvalue=self.used_disk_gb)
            if total and used:
                self.total_disk_gb = total
                self.used_disk_gb = used
                self.usage_pct = (self.used_disk_gb / self.total_disk_gb) * 100
                if self.usage_pct > 90:
                    self.disk_status = "CRITICAL"
                elif self.usage_pct > 75:
                    self.disk_status = "WARNING"
                else:
                    self.disk_status = "OK"
                print("\n[+] Report settings updated successfully.")
        except TypeError:
            print("[-] Configuration cancelled or invalid.")

    def run_health_checks(self):
        run_system_checks()

    def analyze_logs(self):
        analyzeserverlogs()

    def draw_network(self):
        draw_topology(self.manager)

    def ping_device(self):
        hname = simpledialog.askstring("Ping", "Enter Hostname to ping:", parent=self.root)
        if hname:
            dev = self.manager.find_device(hname)
            if dev:
                print(f"\nPinging {hname}...")
                print(dev.ping())
            else:
                print(f"[-] Device '{hname}' not found in inventory.")

    def run_scanner(self):
        target_ip = simpledialog.askstring("Scanner", "Enter target IP (e.g., 127.0.0.1):", parent=self.root)
        if not target_ip:
            return

        start_str = simpledialog.askstring("Scanner", "Enter start port (e.g., 1):", parent=self.root)
        end_str = simpledialog.askstring("Scanner", "Enter end port (e.g., 1024):", parent=self.root)

        start_port = validate_port(start_str)
        end_port = validate_port(end_str)

        if start_port is None or end_port is None or start_port > end_port:
            print("[-] Error: Ports must be valid integers and start must be <= end.")
            return

        # Disable buttons temporarily during scan? (Optional, but good practice)
        print(f"\n[!] GUI Scanner initializing on {target_ip}...")
        self.root.update() # Force UI to update before long scan
        
        try:
            open_ports = scan_target(target_ip, start_port, end_port)
            print("\n[+] Scan Complete.")
            if open_ports:
                for p in open_ports:
                    print(f"  - Port {p} is OPEN")
            else:
                print(f"No open ports found on {target_ip} in range {start_port}-{end_port}.")
        except Exception as e:
            print(f"[-] Scan error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardGUI(root)
    root.mainloop()