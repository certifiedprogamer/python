from tkinter import *
import time
from Ball import *


# video 26: animating multiple objects
window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, "orange")
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()


# video 25: animations
# import time
#
# WIDTH = 500
# HEIGHT = 500
# xVelocity = 2
# yVelocity = 3
# window = Tk()
#
# canvas = Canvas(window, width=WIDTH, height=HEIGHT)
# canvas.pack()
#
# photo_image = PhotoImage(file='garf100.png')
# my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)
#
# image_width = photo_image.width()
# image_height = photo_image.height()
#
# while True:
#     coordinates = canvas.coords(my_image)
#     print(coordinates)
#     if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
#         xVelocity = -xVelocity
#     if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
#         yVelocity = -yVelocity
#     canvas.move(my_image, xVelocity, yVelocity)
#     window.update()
#     time.sleep(0.01)
# window.mainloop()


# video 24 part 2: moving canvases with keyboard
# def move_up(event):
#    canvas.move(myimage, 0, -10)
# def move_down(event):
#    canvas.move(myimage, 0, 10)
# def move_left(event):
#    canvas.move(myimage, -10, 0)
# def move_right(event):
#    canvas.move(myimage, 10, 0)
# window.bind("<w>", move_up)
# window.bind("<s>", move_down)
# window.bind("<a>", move_left)
# window.bind("<d>", move_right)
# canvas = Canvas(window, width=500, height=500)
#
# canvas.pack()
#
# photoimage = PhotoImage(file='garf100.png')
# myimage = canvas.create_image(0, 0, image=photoimage, anchor=NW)
# window.mainloop()


# video 24 part 1: moving images with keyboard
# window.geometry("500x500")
# def move_up(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)
#
#
# def move_left(event):
#    label.place(x=label.winfo_x() - 10, y=label.winfo_y())
#
#
# def move_down(event):
#    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
#
#
# def move_right(event):
#    label.place(x=label.winfo_x() + 10, y=label.winfo_y())
#
#
# window.bind("<w>", move_up)
# window.bind("<a>", move_left)
# window.bind("<s>", move_down)
# window.bind("<d>", move_right)
#
# my_image = PhotoImage(file='garf100.png')
#
# label = Label(window, image=my_image)
# label.place(x=0, y=0)
#
# window.mainloop()

# video 23: GUI drag and drop
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
#
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x, y=y)
#
#
# label = Label(window, bg="red", width=10, height=5)
# label.place(x=0, y=0)
#
# label2 = Label(window, bg="blue", width=10, height=5)
# label2.place(x=100, y=100)
#
# label.bind("<Button-1>", drag_start)
# label.bind("<B1-Motion>", drag_motion)
#
# label2.bind("<Button-1>", drag_start)
# label2.bind("<B1-Motion>", drag_motion)
#
# window.mainloop()


# video 22: mouse events
# def do_something(event):
#     print("mouse coordinates: " + str(event.x) + "," + str(event.y))
#
#
# # window.bind("<Button-1>", do_something)  # left mouse button
# # window.bind("<Button-2>", do_something)  # middle mouse button
# # window.bind("<Button-3>", do_something)  # right mouse button
# # window.bind("<ButtonRelease>", do_something) # triggers when you press and then release any button
# # window.bind("<Enter>", do_something) # enter the window
# # window.bind("<Leave>", do_something)  # leave the window
# window.bind("<Motion>", do_something)  # Where the mouse moved
# window.mainloop()


# - vid 21: keyboard events
# def do_something(event):
#     # print(event.keysym)
#     label.config(text=event.keysym)
#
#
# window.bind("<Key>", do_something)
#
# label = Label(window, font=("Helvetica", 100))
# label.pack()
#
# window.mainloop()


# - vid 20: canvases
# canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill="purple")
# points = [250, 0, 500, 500, 0, 500,]
# canvas.create_polygon(points, fill="yellow", outline="orange", width=2)
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=270, extent=180)
# canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=10)
# canvas.create_arc(0, 0, 500, 500, fill="white",
#                  extent=180, width=10, start=180)
# canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
# canvas.pack()
#
# window.mainloop()


# from tkinter.ttk import *
# import time
# - vid 19: progress bars
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
#
# def start():
#    gb = 50
#    download = 0
#    speed = 2
#    while download < gb:
#        time.sleep(0.05)
#        bar['value'] += (speed/gb) * 100
#        download += speed
#        percent.set(str(int((download/gb) * 100))+"%")
#        text.set(str(download)+"/"+str(gb) + " GB completed")
#        window.update_idletasks()
#
#
# bar = Progressbar(window, orient=HORIZONTAL, length=300)
# bar.pack(pady=10)
#
# percent_label = Label(window, textvariable=percent).pack()
# task_label = Label(window, textvariable=text).pack()
# button = Button(window, text="download", command=start).pack()
#
# window.mainloop()
