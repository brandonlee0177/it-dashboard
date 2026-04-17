# IT Dashboard COP1034C - Week 1 starter script

from datetime import datetime
import logging
debug = True
logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
logging.debug(f"DEBUG: debug={debug}")

APPNAME = "IT Dashboard"
VERSION = "0.1.0"
AUTHOR = "Brandon Lee"
COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
COURSE_NAME = "Programming for Technology Professionals - KU_JAX_COP1034CD4-104062026"
INSTRUCTORS_NAME = "Professor Mora"
ASSIGNMENT_NAME = "Week 1 - IT Dashboard Starter Script"
# Get the current local date and time
currenttime = datetime.now()

# Print the header information
print("-------------------------------- ")
print(f"Author: {AUTHOR}")
print(f"{COPYRIGHT}")
print("-------------------------------- ")
print(f"Course: {COURSE_NAME}")
print(f"Instructor: {INSTRUCTORS_NAME}")
print(f"Assignment: {ASSIGNMENT_NAME}")
print("-------------------------------- ")


# Format as YYYY-MM-DD HH:MM:SS
formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")

print(f"Report generated on: {formattedtime}")

# --- Variable Declarations ---
# String variables for server identity
server_name = "Layla"
ip_address = "10.0.0.1"
department = "New to IT"

# Numeric variables for disk metrics (integers in GB)
total_disk_gb = 70
used_disk_gb = 30

# Float and Boolean for calculations and program state
usage_pct = 0.0
report_ready = True
disk_status = "OK - Disk usage is normal"

def run_system_checks():
    # Iterating through a list of checks using a for loop
    checks = ["CPU Usage", "Memory Usage", "Disk Space", "Network Connectivity"]
    print("System Checks:")
    for check in checks:
        print(f"  - {check}: PASS")  # simulated result

def print_report():
    # --- Report Generation ---
    # Calculate free disk space
    free_disk_gb = total_disk_gb - used_disk_gb
    
    # Using f-string alignment (:<12) to create a clean, table-like layout
    print("====================================")
    print("        IT SYSTEM STATUS REPORT     ")
    print("====================================")
    print(f"{'Server Name':<12}: {server_name}")
    print(f"{'IP Address':<12}: {ip_address}")
    print(f"{'Department':<12}: {department}")
    print("------------------------------------")
    print(f"{'Total Disk':<12}: {total_disk_gb} GB")
    print(f"{'Used Disk':<12}: {used_disk_gb} GB")
    print(f"{'Free Disk':<12}: {free_disk_gb} GB")
    print(f"{'Usage':<12}: {usage_pct:.2f}%")
    print(f"{'Status':<12}: {disk_status}")
    print("====================================")

def analyzeserverlogs():
    """Week 2 Parses server.log and generates logssummary.txt"""
    print("\n--- Running Log Analysis ---")
    # Initialize data structures for log tracking
    severitycounts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
    uniqueerrors = set()
    criticalevents = set()
    logentries = []
    linesread = 0

    import os
    LOGPATH = "server.log"
    LOGPATH = os.environ.get("LOGFILE", LOGPATH)

    try:
        with open(LOGPATH, "r") as f:
            for line in f:
                linesread += 1
                raw = line.rstrip("\n")
                parts = line.strip().split(maxsplit=3)
                if 'debug' in globals() and debug:
                    print(f"DEBUGLINE raw={raw!r} | parts={parts!r} | len(parts)={len(parts)}")
                if len(parts) < 3:
                    continue

                datefield = f"{parts[0]} {parts[1]}"

                severity = None
                message = None

                # Case A: line like "YYYY-MM-DD HH:MM:SS [INFO] Message"
                if len(parts) >= 3 and parts[2].startswith("[") and "]" in parts[2]:
                    end = parts[2].find("]")
                    severity = parts[2][1:end].upper()
                    message = parts[3] if len(parts) > 3 else ""
                # Case B: line where the severity is in parts[3], e.g. "... [INFO] Message"
                elif len(parts) >= 4 and parts[3].startswith("[") and "]" in parts[3]:
                    end = parts[3].find("]")
                    severity = parts[3][1:end].upper()
                    message = parts[3][end+2:]
                else:
                    # Unknown format; skip this line
                    continue

                if severity is None or message is None:
                    continue

                severitycounts[severity] = severitycounts.get(severity, 0) + 1
                if severity == "ERROR":
                    uniqueerrors.add(message)
                if severity == "CRITICAL":
                    criticalevents.add(message)

                logentries.append({ "date": datefield, "severity": severity, "message": message })
    except FileNotFoundError:
        print("Error: server.log not found. Place the log file in the working directory.")
        return

    totallines = linesread
    totalseen = sum(severitycounts.get(s, 0) for s in ["INFO","WARNING","ERROR","CRITICAL"])
    errorrate = (severitycounts.get("ERROR", 0) / totalseen * 100) if totalseen > 0 else 0.0

    with open("logssummary.txt", "w") as out:
        out.write("==================================\n")
        out.write("     SERVER LOG ANALYSIS REPORT     \n")
        out.write("==================================\n")
        out.write(f"Log File : {LOGPATH}\n")
        out.write(f"linesread : {totallines}\n")
        out.write("----------------------------------\n")
        out.write("Severity Counts:\n")
        for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
            out.write(f"  {level:<8}: {severitycounts.get(level, 0):>2}\n")
        out.write("----------------------------------\n")
        out.write(f"ERRORRATE : {errorrate:.2f}%\n")
        out.write("----------------------------------\n")
        out.write(f"UNIQUEERRORS ({len(uniqueerrors)} total)\n")
        for err in sorted(uniqueerrors):
            out.write(f"  - {err}\n")
        out.write(f"CRITICALEVENTS ({len(criticalevents)} total)\n")
        for crit in sorted(criticalevents):
            out.write(f"  - {crit}\n")
        out.write("================================\n")
    print("SUCCESS: Analysis complete. Results written to logssummary.txt")


def main():
    # Pulling in the global variables so the menu can update them
    global server_name, ip_address, department
    global total_disk_gb, used_disk_gb, usage_pct
    global report_ready, disk_status

    print(f"{APPNAME} v{VERSION}")
    print("================================")
    print("Careful spongebob. CAREFUL SPONGEBOB!")

    # --- Main Menu Loop ---
    # Keeps the program running until the user chooses to exit
    while True:
        print("================================")
        print("\n--- IT Report Generator ---")
        print("1) Set Server Info")
        print("2) View Report")
        print("3) Run System Checks")
        print("4) Analyze Server Logs")
        print("5) Exit")
        print("================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            # --- User Input Block ---
            # Ensure defaults exist in the outer scope: server_name, ip_address, department,
            # total_disk_gb, used_disk_gb should be initialized beforehand.
            server_name = input(f"Server Name: ").strip() or server_name
            ip_address = input(f"IP Address: ").strip() or ip_address
            department = input(f"Department: ").strip() or department

            # Disk metrics
            try:
                total_disk_gb = int(input(f"Total Disk (GB): ").strip() or str(total_disk_gb))
                used_disk_gb  = int(input(f"Used Disk (GB): ").strip() or str(used_disk_gb))
            except ValueError:
                print("Invalid input for disk space. Please enter numeric values.")
                continue

            # Edge case handling
            if total_disk_gb < 0 or used_disk_gb < 0 or used_disk_gb > total_disk_gb:
                print("Invalid disk values. Ensure non-negative and used <= total.")
                continue

            # Calculations
            if total_disk_gb > 0:
                usage_pct = (used_disk_gb / total_disk_gb) * 100
            else:
                usage_pct = 0.0

            # Classification
            if usage_pct > 90:
                disk_status = "CRITICAL - Immediate action required"
            elif usage_pct > 75:
                disk_status = "WARNING - Disk usage is elevated"
            else:
                disk_status = "OK - Disk usage is normal"

            # mark that a report can be shown
            report_ready = True

            # Show the report
            print("Data entered. Here is the report:")
            print("================================")
            print(f"Server Name: {server_name}")
            print(f"IP Address: {ip_address}")
            print(f"Department: {department}")
            print(f"Total Disk (GB): {total_disk_gb}")
            print(f"Used Disk (GB): {used_disk_gb}")
            print(f"Usage: {usage_pct:.2f}%")
            print(f"Disk Status: {disk_status}")
            print("================================")

        elif choice == "2":
            if not report_ready:
                print("No data entered yet. Choose option 1 first.")
            else:
                print_report()

        elif choice == "3":
            run_system_checks()

        elif choice == "4":
            analyzeserverlogs()

        elif choice == "5":
            print("Smell ya later stinky.")
            break

        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()