import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def create_scp_window(window):
    window.resizable(False, False)
    tk.Label(window, text="Source:").grid(row=0, column=0, padx=10, sticky=tk.W)
    tk.Label(window, text="Username:").grid(row=1, column=0, pady=10, sticky=tk.W)
    tk.Label(window, text="Host:").grid(row=2, column=0, pady=10, sticky=tk.W)
    tk.Label(window, text="Remote Directory:").grid(row=3, column=0, pady=10, sticky=tk.W)

    source_entry = tk.Entry(window, width=50)
    source_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=lambda: browse(source_entry)).grid(row=0, column=2, padx=5, pady=5)

    username_entry = tk.Entry(window, width=50)
    username_entry.grid(row=1, column=1, padx=5, pady=5)

    host_entry = tk.Entry(window, width=50)
    host_entry.grid(row=2, column=1, padx=5, pady=5)

    remote_dir_entry = tk.Entry(window, width=50)
    remote_dir_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(window, text="Copy Files", command=lambda: copy_files(source_entry.get(), "", username_entry.get(), host_entry.get(), remote_dir_entry.get())).grid(row=4, columnspan=2, pady=10)

def browse(directory_entry):
    path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, path)

def copy_files(source_path, target_path, username, host, remote_dir):
    if not source_path or not username or not host or not remote_dir:
        messagebox.showerror("Error", "All fields are required for SCP.")
        return

    try:
        command = ["scp", "-r", source_path, f"{username}@{host}:{remote_dir}"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", "Files copied successfully using SCP.")
        else:
            messagebox.showerror("Error", f"Failed to copy files using SCP:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
