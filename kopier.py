import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox
from tkinter import ttk


def open_window(method):
    new_window = tk.Toplevel(root)
    new_window.title(method)
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


def create_scp_window(window):
    pass


def create_robocopy_window(window):
    pass


def create_adcpmv_window(window):
    pass


def create_rsync_window(window):
    pass

def create_dd_window(window):
    pass


def copy_files():
    source_path = source_entry.get()
    target_path = target_entry.get()
    parameters = ""
    for option, var in options.items():
        if var.get():
            parameters += option + " "
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


root = tk.Tk()
root.title("Kopier v.0.0.0.4-ALPHA")
root.geometry("700x241")
root.resizable(False, True)

tk.Label(root, text="Source:").grid(row=0, column=0, padx=10)
tk.Label(root, text="Target:").grid(row=1, column=0, pady=10)

source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: browse(source_entry)).grid(row=0, column=2, padx=5)

target_entry = tk.Entry(root, width=50)
target_entry.grid(row=1, column=1, padx=5)
tk.Button(root, text="Browse", command=lambda: browse(target_entry)).grid(row=1, column=2, padx=5)

target_button = tk.Button(root, text="Copy Files", command=copy_files)
target_button.grid(row=4, column=1, pady=10)

output_text = tk.Text(root, height=70, width=70)
output_text.grid(row=5, columnspan=3, pady=10)

source_entry.bind("Control-KeyRelease-a", select_all)
target_entry.bind("Control-KeyRelease-a", select_all)

subdirectories_var = tk.BooleanVar()
empty_subdirectories_var = tk.BooleanVar()
restartable_mode_var = tk.BooleanVar()
backup_mode_var = tk.BooleanVar()
unbuffered_mode_var = tk.BooleanVar()
efsraw_mode_var = tk.BooleanVar()

options = {
    "/s": tk.BooleanVar(),
    "/e": tk.BooleanVar(),
    "/z": tk.BooleanVar(),
    "/b": tk.BooleanVar(),
    "/j": tk.BooleanVar(),
    "/efsraw": tk.BooleanVar()
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
    checkbox = create_checkbox(root, text, options[option])
    checkbox.grid(row=2 + i//3, column=i%3)

root.mainloop()