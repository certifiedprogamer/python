from tkinter import *
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(title="open awesome file",
                                          filetypes=[("comma separated values", "*.csv"),
                                                     ("Excel", "*xlsx"),
                                                     ("All files", "*.*")])
    if filename:
        with open(filename, "r") as file:
            content = file.read()
            print(content)


window = Tk()
Button(text="Open", command=open_file).pack()
window.mainloop()
