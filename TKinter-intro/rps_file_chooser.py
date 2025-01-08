from tkinter import *
from tkinter import filedialog
import os


def save_text():
    directory = filedialog.askdirectory()
    if directory:
        files = os.listdir(directory)

# Filter files if needed (e.g., open only text files)
        files = [f for f in files if f.endswith('.rps')]
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.insert(1.0, f"{content} \n")


window = Tk()
Button(text="Output file", command=save_text).pack()
text_area = Text(window)
text_area.pack()
window.mainloop()
