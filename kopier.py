import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox


def on_button_click():
    source_path = source_entry.get()
    target_path = target_entry.get()
    parameters = ""
    if subdirectories_var.get():
        parameters += "/s "
    if empty_subdirectories_var.get():
        parameters += "/e "
    if restartable_mode_var.get():
        parameters += "/z "
    if backup_mode_var.get():
        parameters += "/b "
    if unbuffered_mode_var.get():
        parameters += "/j "
    if efsraw_mode_var.get():
        parameters += "/efsraw "
    command = f"robocopy {parameters}{source_path} {target_path}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            output_text.insert(tk.END, f"Files copied successfully from {source_path} to {target_path}.")
        else:
            output_text.insert(tk.END, f"Failed to copy files from {source_path} to {target_path}.")
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
    on_button_click()


root = tk.Tk()
root.title("Kopier v.0.0.0.3-ALPHA")
root.geometry("519x241")

source_label = tk.Label(root, text="Source:")
source_label.grid(row=0, column=0, padx=10)

source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5)

source_button = tk.Button(root, text="Browse", command=browse_source)
source_button.grid(row=0, column=2, padx=5)

target_label = tk.Label(root, text="Target:")
target_label.grid(row=1, column=0, pady=10)

target_entry = tk.Entry(root, width=50)
target_entry.grid(row=1, column=1, padx=5)

target_button = tk.Button(root, text="Copy Files", command=on_button_click)
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

subdirectories_checkbox = tk.Checkbutton(root, text="Copy Subdirectories", variable=subdirectories_var)
subdirectories_checkbox.grid(row=2, column=0)

empty_subdirectories_checkbox = tk.Checkbutton(root, text="Copy empty subdirectories", variable=empty_subdirectories_var)
empty_subdirectories_checkbox.grid(row=2, column=1)

restartable_mode_checkbox = tk.Checkbutton(root, text="Restartable mode", variable=restartable_mode_var)
restartable_mode_checkbox.grid(row=2, column=2)

backup_mode_checkbox = tk.Checkbutton(root, text="Backup mode", variable=backup_mode_var)
backup_mode_checkbox.grid(row=3, column=0)

unbuffered_mode_checkbox = tk.Checkbutton(root, text="Unbuffered Mode (Large Files)", variable=unbuffered_mode_var)
unbuffered_mode_checkbox.grid(row=3, column=1)

efsraw_mode_checkbox = tk.Checkbutton(root, text="EFS RAW Mode", variable=efsraw_mode_var)
efsraw_mode_checkbox.grid(row=3, column=2)

root.mainloop()