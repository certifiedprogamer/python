from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)
tab1 = Frame(notebook, bg="red")
tab2 = Frame(notebook, bg="yellow")

notebook.add(tab1, text="First Tab")
notebook.add(tab2, text="Second Tab")

Label(tab1, text="First Tab", width=15, height=5).pack()
Label(tab2, text="Second Tab", width=15, height=5).pack()
notebook.pack(expand=True, fill=BOTH)
window.mainloop()
