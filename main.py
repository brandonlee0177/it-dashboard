# IT Dashboard COP1034C - Week 1 starter script

APPNAME = "IT Dashboard"
VERSION = "0.1.0"

# Global state (initial defaults)
servername = "Layla"
ipaddress = "10.0.0.1"
department = "New to IT"

totaldiskgb = 70
useddiskgb = 30

usagepct = 0.0
reportready = False
diskstatus = "OK - Disk usage is normal"

def run_system_checks():
    checks = ["Ping response", "DNS resolution", "Firewall rule active"]
    print("System Checks:")
    for check in checks:
        print(f"  - {check}: PASS")  # simulated result

def printreport():
    print(f"Server: {servername} ({ipaddress}) - Dept: {department}")
    print(f"Disk Usage: {useddiskgb}/{totaldiskgb} GB ({usagepct:.2f}%) - {diskstatus}")

def main():
    global servername, ipaddress, department
    global totaldiskgb, useddiskgb, usagepct
    global reportready, diskstatus

    print(f"{APPNAME} v{VERSION}")
    print("Ready to build something great.")

    while True:
        print("\n--- IT Report Generator ---")
        print("1) Set Server Info")
        print("2) View Report")
        print("3) Run System Checks")
        print("4) Exit")

        choice=input("Select an option:[1-4] ").strip()

        if choice == "1":
            servername = input(f"Server Name [{servername}]: ").strip() or servername
            ipaddress = input(f"IP Address [{ipaddress}]: ").strip() or ipaddress
            department = input(f"Department [{department}]: ").strip() or department

            try:
                totaldiskgb = int(input(f"Total Disk (GB) [{totaldiskgb}]: ").strip() or totaldiskgb)
                useddiskgb = int(input(f"Used Disk (GB) [{useddiskgb}]: ").strip() or useddiskgb)
            except ValueError:
                print("Invalid input for disk space. Please enter numeric values.")
                continue

            if totaldiskgb < 0 or useddiskgb < 0 or useddiskgb > totaldiskgb:
                print("Invalid disk values. Ensure non-negative and used <= total.")
                continue

            if totaldiskgb > 0:
                usagepct=(useddiskgb / totaldiskgb) * 100
            else:
                usagepct = 0.0

            if usagepct > 90:
                diskstatus = "CRITICAL - Immediate action required"
            elif usagepct > 75:
                diskstatus = "WARNING - Disk usage is elevated"
            else:
                diskstatus = "OK - Disk usage is normal"

            reportready = True
            print("Data entered. You can view the report.")

        elif choice == "2":
            if not reportready:
                print("No data entered yet. Choose option 1 first.")
            else:
                printreport()

        elif choice == "3":
            run_system_checks()

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
