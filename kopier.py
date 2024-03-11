import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox
from tkinter import ttk

output_text = None

def open_window(method):
    if hasattr(root, 'last window'):
        root.last_window.destroy()
    new_window = tk.Toplevel(root)
    new_window.title(method)
    root.last_window = new_window
    if method == "SCP":
        create_scp_window(new_window)
    elif method == "Robocopy":
        create_robocopy_window(new_window)
    elif method == "adcpmv":
        create_adcpmv_window(new_window)
    elif method == "rsync":
        create_rsync_window(new_window)
    elif method == "dd":
        create_dd_window(new_window)


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
    global output_text
    tk.Label(window, text="Source:").grid(row=0, column=0, padx=10)
    tk.Label(window, text="Target:").grid(row=1, column=0, pady=10)

    source_entry = tk.Entry(window, width=50)
    source_entry.grid(row=0, column=1, padx=5)
    tk.Button(window, text="Browse", command=lambda: browse(source_entry)).grid(row=0, column=2, padx=5)

    target_entry = tk.Entry(window, width=50)
    target_entry.grid(row=1, column=1, padx=5)
    tk.Button(window, text="Browse", command=lambda: browse(target_entry)).grid(row=1, column=2, padx=5)

    target_button = tk.Button(window, text="Copy Files", command=lambda: copy_files(source_entry.get(), target_entry.get(), subdirectories_var.get(), empty_subdirectories_var.get(), restartable_mode_var.get(), backup_mode_var.get(), unbuffered_mode_var.get(), efsraw_mode_var.get()))
    target_button.grid(row=3, columnspan=3, pady=10)

    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=4, columnspan=3, pady=10)

    source_entry.bind("<Control-KeyRelease-a>", select_all)
    target_entry.bind("<Control-KeyRelease-a>", select_all)

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

    for i, (text, option) in enumerate(checkboxes):
        checkbox = create_checkbox(window, text, options[option])
        checkbox.grid(row=2 + i//3, column=i%2)


def select_all(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def browse_source():
    source_path = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, tk.END)


def browse_target():
    target_path = filedialog.askdirectory()
    target_entry.delete(0, tk.END)
    target_entry.insert(0, tk.END)


def on_enter(event):
    copy_files()


def browse(directory_entry):
    path = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, path)


def create_checkbox(root, text, var):
    checkbox = tk.Checkbutton(root, text=text, variable=var)
    return checkbox


def create_scp_window(window):
    pass


def create_adcpmv_window(window):
    pass


def create_rsync_window(window):
    pass


def create_dd_window(window):
    pass


root = tk.Tk()
root.title("Kopier v.0.0.0.4-ALPHA")
root.geometry("200x230")
root.resizable(False, False)

options_frame = ttk.LabelFrame(root, text="Select Transfer Method")
options_frame.pack(pady=20)

transfer_methods = ["SCP", "Robocopy", "DD", "adcpmv", "rsync"]

for method in transfer_methods:
    ttk.Button(options_frame, text=method, command=lambda m=method: open_window(m)).pack(pady=5)

root.mainloop()