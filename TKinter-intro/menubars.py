from tkinter import *
import random


def open_file():
    print("GJKIGjn")


def save_file():
    print("savefille1233252323")


def copy():
    print("g()")


def evil():
    for i in range(200):
        top = Toplevel(window)
        rand1 = random.randint(-2000, 2000)
        rand2 = random.randint(-2000, 2000)
        top.geometry("300x150")
        x = window.winfo_x()
        y = window.winfo_y()
        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        top.wm_transient(window)


window = Tk()
window.geometry("400x400")

toplevel_menubar = Menu(window)
window.config(menu=toplevel_menubar)

filemenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)

editmenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="Copy", command=copy)

evilmenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="evil menu", menu=evilmenu)

evilmenu.add_command(label="evil", command=evil)

window.mainloop()
