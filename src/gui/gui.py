import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
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

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background='#333', foreground='#fff', font=('Helvetica', 12))
style.configure('TLabel', background='#333', foreground='#fff', font=('Helvetica', 12))
style.configure('TFrame', background='#333')

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True)

select_button = ttk.Button(frame, text="Select CarX Directory", command=select_directory)
clean_button = ttk.Button(frame, text="Start Cleaning", command=start_cleaning)

select_button.pack(pady=10)
clean_button.pack(pady=10)

root.configure(bg='#333')
root.mainloop()
