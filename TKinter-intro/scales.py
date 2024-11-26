import tkinter as tk

window = tk.Tk()

window.title("volume scale")
window.geometry("400x200")


def set_volume():
    value = scale.get()
    print(f"The volume is {value}")


scale = tk.Scale(window,
                 from_=0,
                 to=100,
                 tickinterval=25,
                 length=200,
                 label="set the volume",
                 orient="horizontal")

button = tk.Button(window, text="Set Volume", command=set_volume)


scale.pack()
button.pack()
window.mainloop()
