import tkinter as tk
import subprocess
from tkinter import filedialog, messagebox


def on_button_click():
    source_path = source_entry.get()
    target_path = target_entry.get()
    command = f"robocopy {source_path} {target_path}"
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
root.title("Kopier v.0.0.0.2-ALPHA")
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
target_button.grid(row=2, column=1, pady=10)

output_text = tk.Text(root, height=70, width=70)
output_text.grid(row=3, columnspan=3, pady=10)

source_entry.bind("Control-KeyRelease-a", select_all)
target_entry.bind("Control-KeyRelease-a", select_all)

root.mainloop()