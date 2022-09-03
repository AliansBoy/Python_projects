import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Notebook')

main = tk.Frame(root)
main.pack(fill='both', expand=True, padx=1, pady=(4,0))

notebook = ttk.Notebook(main)
notebook.pack(fill='both', expand=True)

root.mainloop()
