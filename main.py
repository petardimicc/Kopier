import tkinter as tk
from tkinter import ttk
from scp_transfer import create_scp_window
from robocopy_transfer import create_robocopy_window
from dd_transfer import create_dd_window
from rsync_transfer import create_rsync_window

def open_window(method):
    if hasattr(root, 'last_window'):
        root.last_window.destroy()
    new_window = tk.Toplevel(root)
    new_window.title(method)
    root.last_window = new_window
    if method == "SCP":
        create_scp_window(new_window)
    elif method == "Robocopy":
        create_robocopy_window(new_window)
    elif method == "DD":
        create_dd_window(new_window)
    elif method == "Rsync":
        create_rsync_window(new_window)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kopier v.0.0.0.7-ALPHA")
    root.geometry("200x200")
    root.resizable(False, False)

    options_frame = ttk.LabelFrame(root, text="Select Transfer Method")
    options_frame.pack(pady=20)

    transfer_methods = ["SCP", "Robocopy", "DD", "Rsync"]
    for method in transfer_methods:
        ttk.Button(options_frame, text=method, command=lambda m=method: open_window(m)).pack(pady=5)

    root.mainloop()
