import tkinter as tk
from tkinter import ttk
from scp_transfer import create_scp_window
from robocopy_transfer import create_robocopy_window
from rsync_transfer import create_rsync_window

def open_window(method):
    root.destroy()
    new_window = tk.Toplevel()
    new_window.title(method)
    if method == "SCP":
        create_scp_window(new_window)
    elif method == "Robocopy":
        create_robocopy_window(new_window)
    elif method == "Rsync":
        create_rsync_window(new_window)


root = tk.Tk()
root.title("Kopier v.0.0.0.5-ALPHA")
root.geometry("400x400")
root.resizable(False, False)

options_frame = ttk.LabelFrame(root, text="Select Transfer Method")
options_frame.pack(pady=20)

transfer_methods = ["SCP", "Robocopy", "Rsync"]

for method in transfer_methods:
    ttk.Button(options_frame, text=method, command=lambda m=method: open_window(m)).pack(pady=5)

root.mainloop()
