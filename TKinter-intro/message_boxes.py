import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Message box example")
window.geometry("400x300")


def show_message():
    response = messagebox.askyesno("Yes or no?", "G")
    if response:
        print("yay")
    else:
        print("stupid")


button = tk.Button(window,
                   text="Show Message Box",
                   command=show_message)

button.pack()
window.mainloop()
