from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox


def change_color():
    color = colorchooser.askcolor()
    color_label.config(bg=color[1])
    status_bar.config(text=f"Ship color changed to {color[1]}")


def send_message():
    message = message_alien_pilots.get(1.0, END)
    print(f"Alien Message: {message}")
    status_bar.config(text="Message sent")


def open_file():
    file = filedialog.askopenfile(title="Open File", filetypes=[
                                  ("Text File", "*.txt")])
    print("Contents:")
    print(file.read())
    status_bar.config(text="Uploaded file")


def launch_plan():
    plan = plan_listbox.get(ACTIVE)
    confirm = messagebox.askyesno(
        "Confirmation Message", f"Are you sure you want to launch {plan}?")
    if confirm == True:
        messagebox.showinfo("", f"{plan} launched!")
        status_bar.config(text=f"{plan} has been launched.")
    else:
        messagebox.showinfo("", f"Launch aborted!")
        status_bar.config(text=f"{plan}'s launch has been aborted.")


window = Tk()
window.geometry("600x550")
window.title("Alien Invader HQ Control Panel")
frame_top = Frame(window, bg="green", width=600, height=200)
frame_top.grid_propagate(False)
frame_top.pack()

frame_middle = Frame(window, width=600, height=400)
frame_middle.grid_propagate(False)
frame_middle.pack()

color_label = Label(frame_middle, padx=5, pady=5,
                    width=20, height=6, bg="grey")

spaceship_button = Button(
    frame_middle, text="Change Spaceship Color", padx=5, pady=5, command=change_color)
spaceship_button.grid(row=0, column=0, padx=7, pady=7,)

color_label.grid(row=0, column=0,  padx=7, pady=7,)

message_alien_pilots = Text(frame_middle, width=40, height=6)
message_alien_pilots.grid(row=0, column=1,  padx=5, pady=5,)

message_pilots_button = Button(
    frame_middle, width=10, text="Send Message", command=send_message)
message_pilots_button.grid(row=1, column=1)

upload_file_button = Button(
    frame_middle, text="Upload Secret File", command=open_file)
upload_file_button.grid(row=2, column=0, pady=15)

invasion_label = Label(frame_middle, text="Select Invasion Plan:")
invasion_label.grid(row=2, column=1, pady=15)

plan_listbox = Listbox(frame_middle, width=25, height=5,)

plan_listbox.insert(1, "Plan A: Earth Takeover")
plan_listbox.insert(2, "Plan B: Moon Domination")
plan_listbox.insert(2, "Plan C: Mars Colonization")
plan_listbox.select_set(0)

plan_listbox.grid(row=3, column=1)

launch_button = Button(frame_middle, text="Launch Plan", command=launch_plan)
launch_button.grid(row=4, column=1, pady=7)

frame_bottom = Frame(window, width=600, height=100)
frame_bottom.grid_propagate(False)
frame_bottom.pack()

status_bar = Label(frame_bottom, text="", borderwidth=1,
                   relief="sunken", width=590)
status_bar.pack()

exit_button = Button(frame_bottom, text="Exit", command=exit)
exit_button.pack()

alien_label = Label(frame_top, text="👽", font=("Arial", 32))
alien_label.pack()
window.mainloop()
