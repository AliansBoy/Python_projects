import tkinter as tk
from tkinter import ttk


def greet():
    print('Hello, world!')


def custom_greet():
    print(f"Hello, {user_name.get() or 'World'}")


root = tk.Tk()
root.title("Hello")
user_name = tk.StringVar()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="both", expand=True)

exit_button = ttk.Button(root, text="Quit", command=root.destroy)
exit_button.pack(side="top", fill="x")

name_label = ttk.Label(root, text='Name: ')
name_label.pack(side='left', padx=(0, 10))

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side='left', padx=(0, 10), fill='x', expand=True)
name_entry.focus()

entry_button = ttk.Button(root, text="Enter", command=custom_greet)
entry_button.pack(side='left', fill='x')

root.mainloop()

