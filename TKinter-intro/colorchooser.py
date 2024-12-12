from tkinter import *
from tkinter import colorchooser


def change_bg():
    color = colorchooser.askcolor()
    print(color)
    # color[0] is rgb
    # color[1] is hex
    window.config(background=color[1])


window = Tk()
window.geometry("400x400")

button = Button(text="Change background", command=change_bg)

button.pack()


window.mainloop()
