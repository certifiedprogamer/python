from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def save_text():
    file = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=[(
        "Text File", "*.txt"), ("JSON File", "*.json"), ("CSV File", "*.csv")])
    if file:
        with open(file, "w") as writer:
            writer.write(text_area.get(1.0, END))


def open_file():
    response = "m"
    if text_area.get(1.0, END).strip():
        response = messagebox.askyesno(
            "yesno", "There is already text in there. Would you like to save it?")
        if response == True:
            save_text()
            text_area_write()
        else:
            text_area_write()
    else:
        text_area_write()


def text_area_write():
    text_area.delete(1.0, END)
    file = filedialog.askopenfile(title="Open File", filetypes=[(
        "Text File", "*.txt"), ("JSON File", "*.json"), ("CSV File", "*.csv")])
    if file:
        text_area.insert(1.0, file.read())


window = Tk()
window.geometry("400x400")
window.title("NotePad")
text_area = Text(window)
text_area.pack()
toplevel_menubar = Menu(window)
window.config(menu=toplevel_menubar)

filemenu = Menu(toplevel_menubar, tearoff=0)
toplevel_menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save As", command=save_text)

window.mainloop()
