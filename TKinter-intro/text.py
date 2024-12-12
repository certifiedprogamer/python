from tkinter import *


def check():
    value = text.get(1.0, 1.9)
    print(value)


window = Tk()
text = Text(window,
            height=5,
            width=30,
            font=("Courier New", 24),
            )
text.pack()
button = Button(window, text="check", command=check)
button.pack()
window.mainloop()
