import tkinter as tk


def submit():
    ssn = entry_ssn.get()
    name = entry_name.get()
    print(f"We got {name}'s SSN! {ssn}")
    entry_name.config(state=tk.DISABLED)
    entry_ssn.config(state=tk.DISABLED)


# create a window:
default_font = ("Arial", 16, "bold")

window = tk.Tk()
window.title("Social security scam app")
window.geometry("500x500")  # width x height
icon = tk.PhotoImage(file=r".\resources\imposter.png")
window.iconphoto(True, icon)

label = tk.Label(window,
                 text="Please enter your social security number",
                 font=default_font,
                 )

label.pack()

entry_ssn = tk.Entry(window,
                     font=default_font,
                     width=11,
                     show="*"
                     )
entry_ssn.pack()
# set default text
entry_ssn.insert(0, "555-55-5555")

name_label = tk.Label(window,
                      text="Also enter your name",
                      font=default_font,
                      )
name_label.pack()

entry_name = tk.Entry(window,
                      font=default_font,
                      width=11,
                      )
entry_name.pack()

entry_name.insert(0, "Kerry Sowers")


submit = tk.Button(window,
                   text="Enter",
                   command=submit
                   )
submit.pack()
window.mainloop()
