from tkinter import *
from tkinter import filedialog
from tkinter import ttk
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


root = Tk()
button = Button(text="Output file", command=save_text).pack()
text_area = Text(root, wrap='word', height=10, width=50)
text_area.pack(side=LEFT, fill=BOTH, expand=True)
print(type(text_area))

# Create a Scrollbar widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text_area.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the Text widget to use the Scrollbar
text_area.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()
