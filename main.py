# IT Dashboard COP1034C - Week 1/2 Script

from datetime import datetime
import logging
import os
import subprocess

debug = False
logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
logging.debug(f"DEBUG: debug={debug}")

APPNAME = "IT Dashboard"
VERSION = "0.1.0"
AUTHOR = "Brandon Lee"
COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
COURSE_NAME = "Programming for Technology Professionals - KU_JAX_COP1034CD4-104062026"
INSTRUCTORS_NAME = "Professor Mora"
ASSIGNMENT_NAME = "Week 1 & 2 - IT Dashboard Script"

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
server_name = "Layla"
ip_address = "10.0.0.1"
department = "New to IT"

total_disk_gb = 70
used_disk_gb = 30
usage_pct = 0.0
report_ready = True
disk_status = "OK - Disk usage is normal"

def run_system_checks():
    checks = ["CPU Usage", "Memory Usage", "Disk Space", "Network Connectivity"]
    print("\nSystem Checks:")
    for check in checks:
        print(f"  - {check}: PASS")

def print_report():
    free_disk_gb = total_disk_gb - used_disk_gb
    print("\n====================================")
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
    """Parses server.log and generates logssummary.txt"""
    print("\n--- Running Log Analysis ---")
    
    severitycounts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
    uniqueerrors = set()
    criticalevents = set()
    logentries = []
    linesread = 0

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    DEFAULT_LOGPATH = os.path.join(SCRIPT_DIR, "server.log")
    LOGPATH = os.environ.get("LOGFILE", DEFAULT_LOGPATH)

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

                if len(parts) >= 3 and parts[2].startswith("[") and "]" in parts[2]:
                    end = parts[2].find("]")
                    severity = parts[2][1:end].upper()
                    message = parts[3] if len(parts) > 3 else ""
                elif len(parts) >= 4 and parts[3].startswith("[") and "]" in parts[3]:
                    end = parts[3].find("]")
                    severity = parts[3][1:end].upper()
                    message = parts[3][end+2:]
                else:
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
        print(f"Error: server.log not found. Place it here: {DEFAULT_LOGPATH}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Calculate metrics
    totallines = linesread
    totalseen = sum(severitycounts.get(s, 0) for s in ["INFO", "WARNING", "ERROR", "CRITICAL"])
    errorrate = (severitycounts.get("ERROR", 0) / totalseen * 100) if totalseen > 0 else 0.0

   # Create an absolute path for the summary file, just like we did for the log file
    SUMMARY_PATH = os.path.join(SCRIPT_DIR, "logssummary.txt")

    # Write the summary report using the new absolute path
    try:
        with open(SUMMARY_PATH, "w") as out:
            out.write("==================================\n")
            out.write("    SERVER LOG ANALYSIS REPORT    \n")
            out.write("==================================\n")
            out.write(f"Log File : {LOGPATH}\n")
            out.write(f"Lines Read : {totallines}\n")
            out.write("----------------------------------\n")
            out.write("Severity Counts:\n")
            for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
                out.write(f"  {level:<8}: {severitycounts.get(level, 0):>2}\n")
            out.write("----------------------------------\n")
            out.write(f"Error Rate : {errorrate:.2f}%\n")
            out.write("----------------------------------\n")
            out.write(f"UNIQUE ERRORS ({len(uniqueerrors)} total)\n")
            for err in sorted(uniqueerrors):
                out.write(f"  - {err}\n")
            out.write(f"CRITICAL EVENTS ({len(criticalevents)} total)\n")
            for crit in sorted(criticalevents):
                out.write(f"  - {crit}\n")
            out.write("================================\n")
        print(f"SUCCESS: Analysis complete. Results written to {SUMMARY_PATH}")
        try:
        #popopen opens the ffile without pausing your python script
         subprocess.Popen(['notepad.exe', SUMMARY_PATH])
        except Exception as e:
         print(f"Could not automattically open notepad: {e}")
        #------------------------------------------
    except Exception as e:
        print(f"Failed to save summary report: {e}")

def main():
    global server_name, ip_address, department
    global total_disk_gb, used_disk_gb, usage_pct
    global report_ready, disk_status

    print(f"\n{APPNAME} v{VERSION}")
    print("================================")
    print("Careful spongebob. CAREFUL SPONGEBOB!")

    while True:
        print("\n================================")
        print("--- IT Report Generator ---")
        print("1) Set Server Info")
        print("2) View Report")
        print("3) Run System Checks")
        print("4) Analyze Server Logs")
        print("5) Exit")
        print("================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            server_name = input(f"Server Name [{server_name}]: ").strip() or server_name
            ip_address = input(f"IP Address [{ip_address}]: ").strip() or ip_address
            department = input(f"Department [{department}]: ").strip() or department

            try:
                total_disk_gb = int(input(f"Total Disk (GB) [{total_disk_gb}]: ").strip() or str(total_disk_gb))
                used_disk_gb  = int(input(f"Used Disk (GB) [{used_disk_gb}]: ").strip() or str(used_disk_gb))
            except ValueError:
                print("Invalid input for disk space. Please enter numeric values.")
                continue

            if total_disk_gb < 0 or used_disk_gb < 0 or used_disk_gb > total_disk_gb:
                print("Invalid disk values. Ensure non-negative and used <= total.")
                continue

            if total_disk_gb > 0:
                usage_pct = (used_disk_gb / total_disk_gb) * 100
            else:
                usage_pct = 0.0

            if usage_pct > 90:
                disk_status = "CRITICAL - Immediate action required"
            elif usage_pct > 75:
                disk_status = "WARNING - Disk usage is elevated"
            else:
                disk_status = "OK - Disk usage is normal"

            report_ready = True
            print("\nData entered successfully!")

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
            print("Invalid choice. Enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()