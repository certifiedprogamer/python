# radio buttons
import tkinter as tk
font_info = ("Arial", "20")
window = tk.Tk()
window.title("Class President")
window.geometry("550x300")
label_vote = tk.Label(text="Please make a selection for class president",
                      font=font_info)
label_vote.pack()
vote = tk.StringVar(value="Dakota")


tk.Radiobutton(window, font=font_info, text="James",
               variable=vote, value="James Clark").pack()
tk.Radiobutton(window, font=font_info, text="Coby",
               variable=vote, value="Coby Hughes").pack()
tk.Radiobutton(window, font=font_info, text="Kerry", variable=vote,
               value="Kerry Sowers").pack()


def record_vote():
    label_vote.config(text=f"You voted for {vote.get()}")


tk.Button(window, text="Submit vote", command=record_vote).pack()

window.mainloop()
