from tkinter import *
import random
from playsound import playsound
from threading import Thread
import os
import time

default_font = ("Arial", 20, "bold")


def colorchange():
    while True:
        time.sleep(0.05)
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)
        window.config(bg=_from_rgb((red, blue, green)))


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def start_game():
    button.pack_forget()
    label.pack_forget()
    for i in range(0, 5):
        top = Toplevel(window)
        rand1 = random.randint(-500, 500)
        rand2 = random.randint(-500, 500)
        top.geometry("300x300")
        x = window.winfo_x()
        y = window.winfo_y()
        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        top.resizable(width=False, height=False)
        top.overrideredirect(True)
        top.wm_transient()


default_font = ("Arial", 20, "bold")
window = Tk()

# give the window a title
window.title("Garfield application")
window.resizable(width=False, height=False)
window.overrideredirect(True)

window.geometry("300x300")

label = Label(window, font=default_font, text="3", fg="black")
label.pack(side="top", anchor=CENTER)


def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_reqwidth()) // 2
    y = (screen_height - window.winfo_reqheight()) // 2
    window.geometry(f"+{x}+{y}")


center_window(window)


changer = Thread(target=colorchange)
changer.start()
# create a label
# label = Label(window,text="Garfield is cool",font=default_font,foreground="pink",background="purple",compound="top",bd=20,relief=RAISED,pady=15,padx=25)

# the label will not be there until it is packed.
# label.pack(pady=20)

button = Button(window,
                text="START",
                font=default_font,
                command=start_game,
                activebackground="black",
                activeforeground="white",
                )

button.pack(side='top', anchor='center', pady=100)
window.mainloop()
