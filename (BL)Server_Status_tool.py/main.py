import tkinter as tk
from Window import init_window
from logic import check_status, clear_results, copy_to_clipboard
from widgets import create_ui



if __name__ == "__main__":
    app_root = init_window()
    
    # 1. Build the UI
    # We pass the imported functions (check_status, clear_results) to create_ui
    ip_entry, result_area, status_msg, port_choice = create_ui(
        app_root, 
        check_status, 
        clear_results
    )
    
    # 2. Add the Copy Button
    copy_btn = tk.Button(
        app_root, 
        text="Copy Results", 
        bg="#374151", 
        fg="white",
        command=lambda: copy_to_clipboard(app_root, result_area, status_msg)
    )
    copy_btn.pack(pady=5)

    print("Server Status Tool is running...")
    app_root.mainloop()