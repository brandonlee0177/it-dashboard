import tkinter as tk

def init_window():
    root = tk.Tk()
    root.title("Server Status Tool")
    root.geometry("450x500")
    root.resizable(False, False)
    root.configure(bg="#1a1a2e")
    return root