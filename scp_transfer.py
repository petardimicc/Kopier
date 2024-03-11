import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox, ttk

def copy_files(source_path, target_path, username, host, remote_dir, subdirectories, empty_directories,
               restartable_mode, backup_mode, unbuffered_mode, efsraw_mode, bandwidth_limit=None, compression=False,
               port=None, debugging=False, quiet_mode=False):
    if not source_path or not username or not host or not remote_dir:
        messagebox.showerror("Error", "All fields are required for SCP.")
        return

    parameters = "-r" if subdirectories else ""
    if bandwidth_limit:
        parameters += f" -l {bandwidth_limit}"
    if compression:
        parameters += " -C"
    if port:
        parameters += f" -P {port}"
    if debugging:
        parameters += " -v"
    if quiet_mode:
        parameters += " -q"

    try:
        command = ["scp", parameters, source_path, f"{username}@{host}:{remote_dir}"]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            output_text.insert(tk.END, f"Files copied successfully from {source_path} to {host}:{remote_dir} using SCP.\n")
        else:
            output_text.insert(tk.END, f"Failed to copy files from {source_path} to {host}:{remote_dir} using SCP.\n")
            output_text.insert(tk.END, result.stderr)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def create_scp_window(window):
    window.resizable(False, False)
    global output_text
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

    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=4, columnspan=3, pady=(10, 0))

    tk.Label(window, text="Bandwidth Limit (-l):").grid(row=5, column=0, pady=5, sticky=tk.W)
    bandwidth_limit_var = tk.StringVar()
    bandwidth_limit_checkbox = tk.Checkbutton(window, text="Enable", variable=bandwidth_limit_var, onvalue="",
                                               offvalue="", padx=5)
    bandwidth_limit_checkbox.grid(row=5, column=1, pady=5, sticky=tk.W)
    bandwidth_limit_entry = tk.Entry(window, width=10)
    bandwidth_limit_entry.grid(row=5, column=2, pady=5, sticky=tk.W)

    tk.Label(window, text="Compression (-C):").grid(row=6, column=0, pady=5, sticky=tk.W)
    compression_var = tk.BooleanVar()
    compression_checkbox = tk.Checkbutton(window, text="Enable", variable=compression_var, onvalue=True,
                                           offvalue=False, padx=5)
    compression_checkbox.grid(row=6, column=1, pady=5, sticky=tk.W)

    tk.Label(window, text="Port (-P):").grid(row=7, column=0, pady=5, sticky=tk.W)
    port_entry = tk.Entry(window, width=10)
    port_entry.grid(row=7, column=1, pady=5, sticky=tk.W)

    tk.Label(window, text="Debugging (-V):").grid(row=8, column=0, pady=5, sticky=tk.W)
    debugging_var = tk.BooleanVar()
    debugging_checkbox = tk.Checkbutton(window, text="Enable", variable=debugging_var, onvalue=True, offvalue=False,
                                         padx=5)
    debugging_checkbox.grid(row=8, column=1, pady=5, sticky=tk.W)

    tk.Label(window, text="Quiet Mode (-q):").grid(row=9, column=0, pady=5, sticky=tk.W)
    quiet_mode_var = tk.BooleanVar()
    quiet_mode_checkbox = tk.Checkbutton(window, text="Enable", variable=quiet_mode_var, onvalue=True, offvalue=False,
                                         padx=5)
    quiet_mode_checkbox.grid(row=9, column=1, pady=5, sticky=tk.W)

    tk.Button(window, text="Copy Files",
              command=lambda: copy_files(source_entry.get(), "", username_entry.get(), host_entry.get(),
                                         remote_dir_entry.get(), True, False, False, False, False, False,
                                         bandwidth_limit_entry.get() if bandwidth_limit_var.get() else "",
                                         compression_var.get(), port_entry.get(), debugging_var.get(),
                                         quiet_mode_var.get())).grid(row=10, columnspan=3, pady=10)


def browse(directory_entry):
    path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, path)


def create_checkbox(root, text, var):
    checkbox = tk.Checkbutton(root, text=text, variable=var)
    return checkbox
