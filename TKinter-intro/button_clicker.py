# GUI - graphical user interface
import tkinter as tk
clicks = 0


def on_button_click():
    global clicks
    clicks += 1
    button.config(text=f"Clicks: {clicks}")


default_font = ("Arial", 20, "bold")
window = tk.Tk()
window.title("Clicker")
window.geometry("400x450")
icon = tk.PhotoImage(file=r".\resources\garf.png")
window.iconphoto(True, icon)
window.config(bg="#fedb00")
button = tk.Button(window,
                   text=f"Clicks: {clicks}",
                   font=default_font,
                   command=on_button_click,
                   activebackground="red",
                   activeforeground="green"
                   )
button.pack()
window.mainloop()
