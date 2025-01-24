import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Text Area with Scrollbar")

# Create a Text widget
text_area = tk.Text(root, wrap='word', height=10, width=50)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget to use the Scrollbar
text_area.config(yscrollcommand=scrollbar.set)

# Run the application
root.mainloop()
