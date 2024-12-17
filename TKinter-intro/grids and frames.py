from tkinter import *

# grid - allows layouts to be more tabular like excel.

window = Tk()

frame_left = Frame(window, bg="green", width=200,
                   height=200)
frame_left.grid(row=0, column=0)
# frame_left.grid_propagate(False) #prevent frame resizing based on controls.

frame_right = Frame(window, bg="purple", width=200,
                    height=200)
frame_right.grid(row=0, column=1)

first_name_label = Label(frame_left, text="First Name: ",
                         bg="orange").grid(row=0, column=0)
first_name_entry = Entry(frame_left).grid(row=0, column=1)
first_name_btn = Button(frame_left, text="Click Me").grid(row=0, column=2)

last_name_label = Label(frame_right, text="Last Name: ",
                        bg="pink").grid(row=1, column=0)
last_name_entry = Entry(frame_right).grid(row=1, column=1)

submit_button = Button(window, text="Submit", width=30).grid(
    row=1, column=0, columnspan=2)

window.mainloop()
