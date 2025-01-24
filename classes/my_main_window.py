import tkinter as tk
import my_other_window as other


def open_new_window():
    new_win = tk.Toplevel()
    the_other_win = other.Managed_Window(new_win)


window = tk.Tk()
window.geometry("400x400")
button = tk.Button(text="Open New Window", command=open_new_window).pack()
window.mainloop()
