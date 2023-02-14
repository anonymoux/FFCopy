import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil
import re

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

def browse_src_folder():
    src_path = filedialog.askdirectory()
    src_path_entry.delete(0, tk.END)
    src_path_entry.insert(0, src_path)

def browse_copy_to():
    copy_to = filedialog.askdirectory()
    copy_to_entry.delete(0, tk.END)
    copy_to_entry.insert(0, copy_to)

def compare_names():
    src_path = src_path_entry.get()
    with open(file_path_entry.get(), "r") as f:
        partial_names = re.split(r"[,\n. -]", f.read().strip())
        partial_names = [name.strip() for name in partial_names if name.strip()]
    copy_to_path = copy_to_entry.get()
    files = os.listdir(src_path)
    selected_files = [f for f in files for name in partial_names if name in f]
    same_name_count = 0

    for file in selected_files:
        same_name_count += 1
        shutil.copy(os.path.join(src_path, file), os.path.join(copy_to_path, file))

    tk.messagebox.showinfo("Info", f"{same_name_count} files copied")

root = tk.Tk()
root.title("File Finder&Copy v1.1 by Phat + chatGPT")

file_path_label = tk.Label(root, text="Text file")
file_path_label.grid(row=0, column=0)

file_path_entry = tk.Entry(root, width=50)
file_path_entry.grid(row=0, column=1)

file_browse_button = tk.Button(root, text="Browse", command=browse_file)
file_browse_button.grid(row=0, column=2)

src_path_label = tk.Label(root, text="Source")
src_path_label.grid(row=1, column=0)

src_path_entry = tk.Entry(root, width=50)
src_path_entry.grid(row=1, column=1)

src_browse_button = tk.Button(root, text="Browse", command=browse_src_folder)
src_browse_button.grid(row=1, column=2)

copy_to_label = tk.Label(root, text="Copy To")
copy_to_label.grid(row=2, column=0)

copy_to_entry = tk.Entry(root, width=50)
copy_to_entry.grid(row=2, column=1)

copy_to_browse_button = tk.Button(root, text="Browse", command=browse_copy_to)
copy_to_browse_button.grid(row=2, column=2)

copy_button = tk.Button(root, text="COPY", command=compare_names)
copy_button.grid(row=3, column=1, pady=10)

root.mainloop()
