import tkinter as tk
from tkinter import Toplevel
import random
from playsound import playsound
from threading import Thread
import os
from ctypes import windll

# get the handle to the taskbar
h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)


def play_sound():
    playsound("garfield.mp3")


imgExtension = ["png", "jpeg", "jpg"]  # Image Extensions to be chosen from
allImages = list()


def chooseRandomImage(directory=r"C:\Users\CMP_KeSowers\Desktop\python\TKinter-intro\resources"):
    for img in os.listdir(directory):  # Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice]  # Do Whatever you want with the image file
    return chosenImage


def swag():
    print("B")
    thread = Thread(target=play_sound)
    thread.start()
    windll.user32.ShowWindow(h, 0)
    for i in range(0, 2000):
        top = Toplevel(window)
        rand1 = random.randint(-2000, 2000)
        rand2 = random.randint(-2000, 2000)
        top.geometry("300x150")
        top.overrideredirect(True)
        x = window.winfo_x()
        y = window.winfo_y()
        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        # top_photo = tk.PhotoImage(
        #    file=r"C:\Users\CMP_KeSowers\Desktop\python\TKinter-intro\resources\garf100.png")
        # top_label = tk.Label(top, image=top_photo)
        # top_label.pack()
        top.wm_transient()


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
icon = tk.PhotoImage(
    file=r"C:\Users\CMP_KeSowers\Desktop\python\TKinter-intro\resources\garf100.png")
window.iconphoto(True, icon)

# change background color of window
window.config(bg="#fedb00")


# create a label
photo = tk.PhotoImage(
    file=r"C:\Users\CMP_KeSowers\Desktop\python\TKinter-intro\resources\garf100.png")
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
