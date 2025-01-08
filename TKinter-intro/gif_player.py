import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random


class GIFPlayer(tk.Label):
    def __init__(self, master, gif_path):
        super().__init__(master)
        self.gif_path = gif_path
        self.frames = [ImageTk.PhotoImage(
            img) for img in ImageSequence.Iterator(Image.open(gif_path))]
        self.current_frame = 0
        self.update_frame()

    def update_frame(self):
        self.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(100, self.update_frame)  # Adjust the delay as needed


def main():
    for i in range(0, 50):
        top = tk.Toplevel(window)
        rand1 = random.randint(-1000, 1000)
        rand2 = random.randint(-1000, 1000)
        top.geometry("300x150")
        x = window.winfo_x()
        y = window.winfo_y()
        gif_player = GIFPlayer(top, "garfieldbreakdancing.gif")
        gif_player.pack()
        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        # top_photo = tk.PhotoImage(
        #    file=r"C:\Users\CMP_KeSowers\Desktop\python\TKinter-intro\resources\garf100.png")
        # top_label = tk.Label(top, image=top_photo)
        # top_label.pack()
        top.wm_transient()


window = tk.Tk()
window.title("GIF Player")
gif_player = GIFPlayer(window, "garfieldbreakdancing.gif")
gif_player.pack()
button = tk.Button(text="g", command=main).pack()
window.mainloop()
