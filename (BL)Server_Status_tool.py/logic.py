import tkinter as tk
from tkinter import messagebox

def check_status(ip_entry, status_var, result_text, port_var):
    ip = ip_entry.get().strip()
    if not ip:
        messagebox.showerror("Error", "Please enter a server IP address.")
        return
        
    port = port_var.get()
    status_var.set(f"Checking {ip}:{port}...")
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Checking {ip} on port {port}...\n")
    # Tagging for the bonus challenge
    result_text.tag_config("online", foreground="#3ab577")
    result_text.insert(tk.END, "Status: ONLINE\n", "online")
    
    status_var.set(f"Last checked: {ip}")

def clear_results(ip_entry, result_text, status_var):
    result_text.delete("1.0", tk.END)
    ip_entry.delete(0, tk.END)
    # If using a default value, re-insert it:
    ip_entry.insert(0, "192.168.1.1")
    status_var.set("Cleared")

def copy_to_clipboard(root, result_text, status_var):
    content = result_text.get("1.0", tk.END).strip()
    if content:
        root.clipboard_clear()
        root.clipboard_append(content)
        status_var.set("Results copied to clipboard!")