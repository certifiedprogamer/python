# a frame is a rectangular container to group and hold widgets
from tkinter import *

window = Tk()
window.geometry("400x400")
frame = Frame(window, bg="yellow")

frame.place(x=100, y=100)

Button(frame, text="W", width=3).pack(side=TOP)
Button(frame, text="A", width=3).pack(side=LEFT)
Button(frame, text="S", width=3).pack(side=LEFT)
Button(frame, text="D", width=3).pack(side=LEFT)

window.mainloop()
