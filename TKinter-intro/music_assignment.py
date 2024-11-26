import tkinter as tk
from tkinter import messagebox

default_font = ("Arial", 13)

window = tk.Tk()
window.title("My Music Preferences")
window.geometry("400x500")


def submit_preferences():
    artist = artist_enter.get()
    genres_list = list()
    genres = check_rock.get(), check_pop.get(), check_jazz.get()
    if genres[0] == 1:
        genres_list.append("Rock")
    if genres[1] == 1:
        genres_list.append("Pop")
    if genres[2] == 1:
        genres_list.append("Jazz")
    listening_method = method.get()
    messagebox.showinfo("Music preferences", f"Favorite artist/band: {artist} \n Favorite genres: {
        genres_list} \n Preferred listening method: {listening_method}")


label_welcome = tk.Label(window,
                         text="Welcome to My Music Preferences!",
                         font=("Arial", 15),
                         foreground="purple")
label_artist = tk.Label(window,
                        text="Who is your favorite artist or band?",
                        font=default_font,
                        )

artist_enter = tk.Entry(window,
                        width=20)

label_genres = tk.Label(window,
                        text="Select your favorite music genres:",
                        font=default_font)

# initializes checkboxes
check_rock = tk.IntVar()

checkbox_rock = tk.Checkbutton(window,
                               text="Rock",
                               variable=check_rock)

check_pop = tk.IntVar()

checkbox_pop = tk.Checkbutton(window,
                              text="Pop",
                              variable=check_pop)

check_jazz = tk.IntVar()

checkbox_jazz = tk.Checkbutton(window,
                               text="jazz",
                               variable=check_jazz)

label_method = tk.Label(window,
                        text="Choose your preferred listening method:",
                        font=default_font,
                        )

submit_button = tk.Button(window,
                          text="Submit",
                          bg="blue",
                          fg="white",
                          command=submit_preferences)
method = tk.StringVar(value="Streaming")
# packs everything into the window
label_welcome.pack()
label_artist.pack()
artist_enter.pack()
label_genres.pack()
checkbox_rock.pack(anchor="w")
checkbox_pop.pack(anchor="w")
checkbox_jazz.pack(anchor="w")
label_method.pack()
tk.Radiobutton(window, text="Streaming",
               variable=method, value="Streaming").pack(anchor="w")
tk.Radiobutton(window, text="CDs",
               variable=method, value="CDs").pack(anchor="w")
tk.Radiobutton(window, text="Vinyl", variable=method,
               value="Vinyl").pack(anchor="w")
submit_button.pack()
window.mainloop()
