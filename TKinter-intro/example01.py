# GUI - graphical user interface
import tkinter as tk


def on_button_click():
    print("Button was clicked!")
    label.config(text="Arnold is better")
    photo.config(file=r".\resources\arnold.png")


default_font = ("Arial", 20, "bold")
window = tk.Tk()

# give the window a title
window.title("Garfield application")


# set the size of the window
window.geometry("400x450")  # width x height

# change the icon in the top left
icon = tk.PhotoImage(file=r".\resources\garf.png")
window.iconphoto(True, icon)

# change background color of window
window.config(bg="#fedb00")


# create a label
photo = tk.PhotoImage(file=r".\resources\garf100.png")
label = tk.Label(window,
                 text="Garfield is cool",
                 font=default_font,
                 foreground="pink",
                 background="purple",
                 image=photo,
                 compound="top",
                 bd=20,
                 relief=tk.RAISED,
                 pady=15,
                 padx=25)

# the label will not be there until it is packed.
label.pack(pady=20)

button = tk.Button(window,
                   text="How about Arnold?",
                   font=default_font,
                   command=on_button_click,
                   activebackground="red",
                   activeforeground="green"
                   )
button.pack()
window.mainloop()
