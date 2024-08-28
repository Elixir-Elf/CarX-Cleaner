import tkinter as tk
from tkinter import filedialog
from src.cleaner.cleaner import start_cleaning_process

def select_directory():
    directory = filedialog.askdirectory()
    return directory

def start_cleaning():
    directory = select_directory()
    if directory:
        start_cleaning_process(directory)

root = tk.Tk()
root.title("CarX Cleaner")
root.geometry("600x500")

select_button = tk.Button(root, text="Select CarX Directory", command=select_directory)
clean_button = tk.Button(root, text="Start Cleaning", command=start_cleaning)

select_button.pack(pady=10)
clean_button.pack(pady=10)

root.mainloop()
