import os
import subprocess
from datetime import datetime

# --- SYSTEM FUNCTIONS (LEGACY CORE) ---

def run_system_checks():
    """Simulates real-time system health checks via loop iteration."""
    checks = ["CPU Usage", "Memory Usage", "Disk Space", "Network Connectivity", "Firewall Status"]
    print("\n[!] Running System Integrity Checks...")
    for check in checks:
        print(f"  - {check:<22}: [ PASS ]")
    print("[+] All system checks completed successfully.")

def print_report(server_name, ip, dept, total, used, usage_pct, status):
    """Displays the high-detail IT System Status Report."""
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
    """Parses 'server.log' and generates 'logssummary.txt'."""
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
        subprocess.Popen(['notepad.exe', SUMMARY_PATH])

    except Exception as e:
        print(f"An unexpected error occurred during analysis: {e}")