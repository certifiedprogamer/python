import tkinter as tk
from tkinter import Toplevel
import random


def swag():
    print("B")
    for i in range(0, 2000):
        top = Toplevel(window)
        rand1 = random.randint(-2000, 2000)
        rand2 = random.randint(-2000, 2000)
        top.geometry("300x150")
        x = window.winfo_x()
        y = window.winfo_y()
        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        top.wm_transient(window)


default_font = ("Arial", 20, "bold")
window = tk.Tk()

# give the window a title
window.title("Garfield application")
window.resizable(width=False, height=False)
window.overrideredirect(True)


def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")


center_window(window)

# change the icon in the top left
icon = tk.PhotoImage(file=r".\resources\garf.png")
window.iconphoto(True, icon)

# change background color of window
window.config(bg="#fedb00")


# create a label
photo = tk.PhotoImage(file=r".\resources\garf100.png")
label = tk.Label(window,
                 text="Garfield is cool",
                 font=default_font,
                 foreground="pink",
                 background="purple",
                 image=photo,
                 compound="top",
                 bd=20,
                 relief=tk.RAISED,
                 pady=15,
                 padx=25)

# the label will not be there until it is packed.
label.pack(pady=20)

button = tk.Button(window,
                   text="True....",
                   font=default_font,
                   command=swag,
                   activebackground="red",
                   activeforeground="green"
                   )
button.pack()
window.mainloop()
