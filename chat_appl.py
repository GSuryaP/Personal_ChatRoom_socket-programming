import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import socket
import threading
import time
from datetime import datetime

class NetworkChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UDP Chat Tool")
        
        # Set to full screen
        self.root.attributes("-zoomed", True)
        
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left side - Chat area
        self.chat_frame = ttk.Frame(self.main_frame, padding=10)
        self.chat_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        ttk.Label(self.chat_frame, text="Chat Window", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.message_display = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, height=25, font=("Arial", 12))
        self.message_display.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.message_display.config(state='disabled')
        
        # Message input
        self.input_frame = ttk.Frame(self.chat_frame)
        self.input_frame.grid(row=2, column=0, sticky="ew", pady=5)
        
        self.message_entry = ttk.Entry(self.input_frame, font=("Arial", 12))
        self.message_entry.grid(row=0, column=0, sticky="ew", padx=5)
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_btn = tk.Button(self.input_frame, text="Send", command=lambda: self.send_message(None), bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.RAISED)
        self.send_btn.grid(row=0, column=1, padx=5)
        
        self.input_frame.columnconfigure(0, weight=1)
        
        # Right side - Settings & Stats
        self.right_panel = ttk.Frame(self.main_frame, padding=10)
        self.right_panel.grid(row=0, column=1, sticky="ns", padx=20, pady=10)
        
        ttk.Label(self.right_panel, text="UDP Settings", font=("Arial", 14, "bold")).grid(row=0, column=0, pady=10)
        
        ttk.Label(self.right_panel, text="IP Address:").grid(row=1, column=0, sticky="w", pady=5)
        self.ip_entry = ttk.Entry(self.right_panel, font=("Arial", 12))
        self.ip_entry.insert(0, "192.168.1.1")
        self.ip_entry.grid(row=2, column=0, pady=5)
        
        ttk.Label(self.right_panel, text="Port:").grid(row=3, column=0, sticky="w", pady=5)
        self.port_entry = ttk.Entry(self.right_panel, font=("Arial", 12))
        self.port_entry.insert(0, "12345")
        self.port_entry.grid(row=4, column=0, pady=5)
        
        self.start_btn = tk.Button(self.right_panel, text="Start Chat", command=self.initialize_udp, bg="#008CBA", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.RAISED)
        self.start_btn.grid(row=5, column=0, pady=10)
        
        # Theme toggle button
        self.theme_toggle_btn = tk.Button(self.right_panel, text="Toggle Theme", command=self.toggle_theme, bg="#f39c12", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, relief=tk.RAISED)
        self.theme_toggle_btn.grid(row=6, column=0, pady=10)
        
        # Status Bar
        self.status_label = ttk.Label(self.root, text="Status: Not Connected", anchor="w", font=("Arial", 10))
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Grid layout configuration
        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=1)
        self.chat_frame.columnconfigure(0, weight=1)
        
        # Initialize theme after widgets are created
        self.current_theme = "dark"
        self.set_theme(self.current_theme)
    
    def set_theme(self, theme):
        style = ttk.Style()
        if theme == "dark":
            style.configure("TFrame", background="#1E1E1E")
            style.configure("TLabel", background="#1E1E1E", foreground="white", font=("Arial", 12))
            self.message_display.config(bg="#252526", fg="white")
            self.status_label.config(background="#333", foreground="white")
        else:
            style.configure("TFrame", background="#F0F0F0")
            style.configure("TLabel", background="#F0F0F0", foreground="black", font=("Arial", 12))
            self.message_display.config(bg="#FFFFFF", fg="black")
            self.status_label.config(background="#DDD", foreground="black")
    
    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.set_theme(self.current_theme)
    
    def initialize_udp(self):
        self.status_label.config(text="Status: Chat Started")
    
    def send_message(self, event):
        message = self.message_entry.get().strip()
        if message:
            self.message_display.config(state='normal')
            self.message_display.insert(tk.END, "You: " + message + "\n")
            self.message_display.config(state='disabled')
            self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkChatApp(root)
    root.mainloop()
