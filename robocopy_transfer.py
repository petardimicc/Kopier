import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def create_robocopy_window(window):
    window.resizable(False, False)
    tk.Label(window, text="Source:").grid(row=0, column=0, padx=10, sticky=tk.W)
    tk.Label(window, text="Target:").grid(row=1, column=0, pady=10, sticky=tk.W)

    source_entry = tk.Entry(window, width=50)
    source_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=lambda: browse(source_entry)).grid(row=0, column=2, padx=5, pady=5)

    target_entry = tk.Entry(window, width=50)
    target_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=lambda: browse(target_entry)).grid(row=1, column=2, padx=5, pady=5)

    tk.Button(window, text="Copy Files", command=lambda: copy_files(source_entry.get(), target_entry.get())).grid(row=2, columnspan=3, pady=10)

def browse(directory_entry):
    path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, path)

def copy_files(source_path, target_path):
    if not source_path or not target_path:
        messagebox.showerror("Error", "Source and target paths are required for Robocopy.")
        return

    try:
        command = f"robocopy {source_path} {target_path}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Success", "Files copied successfully using Robocopy.")
        else:
            messagebox.showerror("Error", f"Failed to copy files using Robocopy:\n{result.stderr}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
