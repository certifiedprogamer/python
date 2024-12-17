from tkinter import *
# grid - allows layouts to be more tabular like excel
window = Tk()

first_name_label = Label(window, text="First Name",
                         bg="orange").grid(row=0, column=0)
first_name_entry = Entry(window).grid(row=0, column=1)

first_name_button = Button(window, text="Click me").grid(row=0, column=2)

last_name_label = Label(window, text="First Name",
                        bg="pink").grid(row=1, column=0)
last_name_entry = Entry(window).grid(row=1, column=1)

submit_button = Button(window, text="Submit", width=30).grid(
    row=2, column=0, columnspan=3)
window.mainloop()
