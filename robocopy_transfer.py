import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox, ttk

def copy_files(source_path, target_path, subdirectories, empty_directories, restartable_mode, backup_mode, unbuffered_mode, efsraw_mode):
    parameters = ""
    if subdirectories:
        parameters += "/s "
    if empty_directories:
        parameters += "/e "
    if restartable_mode:
        parameters += "/z "
    if backup_mode:
        parameters += "/b "
    if unbuffered_mode:
        parameters += "/j "
    if efsraw_mode:
        parameters += "/efsraw "
    command = f"robocopy {parameters}{source_path} {target_path}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        if result.returncode == 0:
            output_text.insert(tk.END, f"Files copied successfully from {source_path} to {target_path}.")
        else:
            output_text.insert(tk.END, f"Failed to copy files from {source_path} to {target_path}.")
        output_text.insert(tk.END, output)
    except Exception as e:
        messagebox.showerror("Error?", str(e))


def create_robocopy_window(window):
    window.resizable(False, False)
    global output_text
    tk.Label(window, text="Source:").grid(row=0, column=0, padx=10, sticky=tk.W)
    tk.Label(window, text="Target:").grid(row=1, column=0, pady=10, sticky=tk.W)

    source_entry = tk.Entry(window, width=50)
    source_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=lambda: browse(source_entry)).grid(row=0, column=2, padx=5, pady=5)

    target_entry = tk.Entry(window, width=50)
    target_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(window, text="Browse", command=lambda: browse(target_entry)).grid(row=1, column=2, padx=5, pady=5)

    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=2, columnspan=3, pady=(10, 0))

    global subdirectories_var, empty_subdirectories_var, restartable_mode_var, backup_mode_var, unbuffered_mode_var, efsraw_mode_var

    subdirectories_var = tk.BooleanVar()
    empty_subdirectories_var = tk.BooleanVar()
    restartable_mode_var = tk.BooleanVar()
    backup_mode_var = tk.BooleanVar()
    unbuffered_mode_var = tk.BooleanVar()
    efsraw_mode_var = tk.BooleanVar()

    options = {
        "/s": subdirectories_var,
        "/e": empty_subdirectories_var,
        "/z": restartable_mode_var,
        "/b": backup_mode_var,
        "/j": unbuffered_mode_var,
        "/efsraw": efsraw_mode_var
    }

    checkboxes = {
        ("Copy Subdirectories", "/s"),
        ("Copy empty Subdirectories", "/e"),
        ("Restartable mode", "/z"),
        ("Backup mode", "/b"),
        ("Unbuffered Mode (Large Files)", "/j"),
        ("EFS RAW Mode", "/efsraw"),
    }

    num_columns = 2
    row = 3
    column = 0
    for text, option in checkboxes:
        checkbox = create_checkbox(window, text, options[option])
        checkbox.grid(row=row, column=column, sticky=tk.W, padx=10, pady=5)
        column += 1
        if column >= num_columns:
            column = 0
            row += 1

    tk.Button(window, text="Copy Files", command=lambda: copy_files(source_entry.get(), target_entry.get(), subdirectories_var.get(), empty_subdirectories_var.get(), restartable_mode_var.get(), backup_mode_var.get(), unbuffered_mode_var.get(), efsraw_mode_var.get())).grid(row=row, columnspan=2, pady=10)

def create_checkbox(root, text, var):
    checkbox = ttk.Checkbutton(root, text=text, variable=var)
    return checkbox