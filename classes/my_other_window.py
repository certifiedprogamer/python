import tkinter as tk


class Managed_Window():
    def __init__(self, window: tk.Tk):
        """Accepts a window which will be managed by this class"""
        self.root = window
        self.root.title("A window managed in a class")
        self.root.geometry("300x300")
        lbl = tk.Label(self.root, text="I'm a label in a window in a class")
        lbl.pack()


if __name__ == "__main__":
    window = tk.Tk()
    my_win = Managed_Window(window)

    window.mainloop()
