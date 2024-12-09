import tkinter as tk
from tkinter import messagebox

default_font = ("Arial", 13)

window = tk.Tk()
window.title("Event Planner")
window.geometry("500x700")
window.resizable(width=False, height=False)


def submit_preferences():
    event = event_enter.get()
    preferences_list = list()
    preferences = check_catering.get(), check_music.get(), check_streaming.get()
    found = False
    if preferences[0] == 1:
        preferences_list.append("Catering")
        found = True
    if preferences[1] == 1:
        preferences_list.append("Music")
        found = True
    if preferences[2] == 1:
        preferences_list.append("Online Streaming")
        found = True
    if found == False:
        preferences_list.append("None")
    event_type = type.get()
    guest_count = scale_guests.get()
    event_theme = listbox_theme.get(tk.ACTIVE)
    messagebox.showinfo("Event Summary", f" \n Event Name: {event} \n Event Type: {
                        event_type} \n Preferences: {", ".join(preferences_list)} \n Number of Guests: {guest_count} \n Event Theme: {event_theme}")


def reset_selection():
    event_enter.delete(0, tk.END)
    check_catering.set(1)
    check_music.set(0)
    check_streaming.set(0)
    type.set("Wedding")
    scale_guests.set(0)
    listbox_theme.select_set(0)


label_plan = tk.Label(window,
                      text="Plan Your Event",
                      font=("Arial", 15),
                      foreground="Blue")
label_event_name = tk.Label(window,
                            text="Enter the Event Name:",
                            font=default_font,
                            )

event_enter = tk.Entry(window,
                       width=20)

label_preferences = tk.Label(window,
                             text="Select Preferences:",
                             font=default_font)

# initializes checkboxes
check_catering = tk.IntVar(value=True)

checkbox_catering = tk.Checkbutton(window,
                                   text="Include Catering",
                                   variable=check_catering
                                   )

check_music = tk.IntVar()

checkbox_music = tk.Checkbutton(window,
                                text="Provide Music",
                                variable=check_music)

check_streaming = tk.IntVar()

checkbox_streaming = tk.Checkbutton(window,
                                    text="Enable Online Streaming",
                                    variable=check_streaming)

label_type = tk.Label(window,
                      text="Select Event Type:",
                      font=default_font,
                      )


label_guests = tk.Label(window,
                        text="Number of Guests:",
                        font=default_font,
                        )

scale_guests = tk.Scale(window,
                        from_=0,
                        to=500,
                        tickinterval=50,
                        length=500,
                        orient="horizontal")

label_theme = tk.Label(window,
                       text="Select Event Theme:",
                       font=default_font,
                       )

listbox_theme = tk.Listbox(window, width=20, height=5, font=default_font,)

listbox_theme.insert(1, "Modern")
listbox_theme.insert(2, "Classic")
listbox_theme.insert(3, "Rustic")
listbox_theme.insert(4, "Futuristic")
listbox_theme.select_set(0)
type = tk.StringVar(value="Wedding")
# packs everything into the window
label_plan.pack()
label_event_name.pack()
event_enter.pack()
label_preferences.pack()
checkbox_catering.pack(anchor="w")
checkbox_music.pack(anchor="w")
checkbox_streaming.pack(anchor="w")
label_type.pack()
tk.Radiobutton(window, text="Wedding",
               variable=type, value="Wedding").pack(anchor="w")
tk.Radiobutton(window, text="Conference",
               variable=type, value="Conference").pack(anchor="w")
tk.Radiobutton(window, text="Birthday Party", variable=type,
               value="Birthday Party").pack(anchor="w")
label_guests.pack()
scale_guests.pack()
label_theme.pack()
listbox_theme.pack()

submit_button = tk.Button(window,
                          text="Submit",
                          bg="green",
                          fg="white",
                          font=("Arial", 10),
                          width=8,
                          command=submit_preferences)
reset_button = tk.Button(window,
                         text="Reset",
                         bg="red",
                         fg="white",
                         font=("Arial", 10),
                         width=8,
                         command=reset_selection)
submit_button.pack(side="left", anchor="e", padx=5, expand=True)
reset_button.pack(side="right", anchor="w", padx=5, expand=True)
window.mainloop()
