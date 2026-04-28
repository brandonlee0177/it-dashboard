import tkinter as tk

def create_ui(root, check_func, clear_func):
    """
    Builds the Server Status Tool UI.
    Returns: ip_entry, result_text, status_var, port_var
    """
    
    # --- 1. TITLE (Step 2) ---
    title_label = tk.Label(
        root, text="Server Status Tool",
        font=("Arial", 18, "bold"), fg="#c9a83a", bg="#1a1a2e"
    )
    title_label.pack(pady=15)

    # --- 2. INPUT AREA & PORT DROPDOWN (Step 3 & Bonus 1) ---
    input_frame = tk.Frame(root, bg="#1a1a2e")
    input_frame.pack(pady=10)

    # IP Label and Entry
    tk.Label(input_frame, text="Server IP:", font=("Arial", 11), 
             fg="white", bg="#1a1a2e").grid(row=0, column=0, padx=5)
    
    ip_entry = tk.Entry(input_frame, width=25, font=("Consolas", 11))
    ip_entry.grid(row=0, column=1, padx=5)
    ip_entry.insert(0, "192.168.1.1")

    # Bonus: Port Dropdown
    port_options = ["80", "443", "22", "8080", "3389"]
    port_var = tk.StringVar(value=port_options[0])
    
    tk.Label(input_frame, text="Port:", font=("Arial", 11), 
             fg="white", bg="#1a1a2e").grid(row=1, column=0, padx=5, pady=5)
    
    port_menu = tk.OptionMenu(input_frame, port_var, *port_options)
    port_menu.config(bg="#374151", fg="white", font=("Consolas", 10), width=10)
    port_menu.grid(row=1, column=1, padx=5, sticky="w")

    # --- 3. BUTTONS (Step 7) ---
    btn_frame = tk.Frame(root, bg="#1a1a2e")
    btn_frame.pack(pady=10)

    # Check Button - Notice we pass port_var here too!
    check_btn = tk.Button(
        btn_frame, text="Check Status",
        command=lambda: check_func(ip_entry, status_var, result_text, port_var),
        bg="#c9a83a", fg="#000", font=("Arial", 11, "bold"), 
        width=15, cursor="hand2"
    )
    check_btn.grid(row=0, column=0, padx=5)

    # Clear Button
    clear_btn = tk.Button(
        btn_frame, text="Clear",
        command=lambda: clear_func(ip_entry, result_text, status_var),
        bg="#374151", fg="white", font=("Arial", 11), 
        width=10, cursor="hand2"
    )
    clear_btn.grid(row=0, column=1, padx=5)

    # --- 4. RESULTS AREA (Step 5) ---
    result_text = tk.Text(
        root, width=50, height=8, font=("Consolas", 10),
        bg="#0d1117", fg="#3ab577", relief="sunken"
    )
    result_text.pack(padx=20, pady=5)

    # --- 5. STATUS BAR (Step 6) ---
    status_var = tk.StringVar(value="Ready")
    status_bar = tk.Label(
        root, textvariable=status_var, font=("Arial", 9),
        fg="#64748b", bg="#12121e", anchor="w", padx=10
    )
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # --- 6. KEYBOARD BINDING (Step 9) ---
    ip_entry.bind("<Return>", lambda e: check_func(ip_entry, status_var, result_text, port_var))

    # Return all 4 items to main.py
    return ip_entry, result_text, status_var, port_var