import tkinter as tk
from tkinter import filedialog, ttk, messagebox

output_text = None


def copy_files(source_path, target_path, block_size, count):
    pass


def create_dd_window(root):
    window = tk.Toplevel(root)
    window.title("DD Transfer")
    window.resizable(False, False)

    tk.Label(window, text="Source:").grid(row=0, column=0, padx=10, sticky=tk.W)

    global output_text
    output_text = tk.Text(window, height=10, width=50)
    output_text.grid(row=2, columnspan=3, pady=(10, 0))

    tk.Button(window, text="Copy Files", command=lambda: copy_files()).grid(row=10, columnspan=3, pady=10)

    return window


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kopier v.0.0.0.4-ALPHA")
    root.geometry("400x400")
    root.resizable(False, False)

    options_frame = ttk.LabelFrame(root, text="Select Transfer Method")
    options_frame.pack(pady=20)

    transfer_methods = ["DD"]
    for method in transfer_methods:
        ttk.Button(options_frame, text=method, command=lambda m=method: create_dd_window(root)).pack(pady=5)

    root.mainloop()
