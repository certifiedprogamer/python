import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random


class GIFPlayer(tk.Label):
    frames = {}  # Store frames globally for each GIF

    def __init__(self, master, gif_path):
        super().__init__(master)
        # Load frames only if not already loaded for the specific GIF
        if gif_path not in GIFPlayer.frames:
            GIFPlayer.frames[gif_path] = [ImageTk.PhotoImage(
                img) for img in ImageSequence.Iterator(Image.open(gif_path))]

        self.frames = GIFPlayer.frames[gif_path]
        self.current_frame = 0
        self.update_frame()

    def update_frame(self):
        # Update the image with the next frame
        self.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(100, self.update_frame)  # Adjust the delay as needed


def main():
    # List of available GIFs
    gifs = ["garfieldbreakdancing.gif", "garfieldeat.gif", "devious smile.gif"]

    # Limit the number of windows to a reasonable number (e.g., 50)
    for i in range(800):
        top = tk.Toplevel(window)
        rand1 = random.randint(-1000, 1000)
        rand2 = random.randint(-1000, 1000)
        top.geometry("300x150")

        # Randomly select a GIF for each window
        gif_path = random.choice(gifs)

        x = window.winfo_x()
        y = window.winfo_y()

        # Create the GIF player with the random GIF
        gif_player = GIFPlayer(top, gif_path)
        gif_player.pack()

        top.geometry("+%d+%d" % (x+rand1, y+rand2))
        top.wm_transient()


window = tk.Tk()
window.title("GIF Player")

# Add a default GIF player in the main window
gif_player = GIFPlayer(window, "garfieldbreakdancing.gif")
gif_player.pack()

# Button to trigger creation of random GIF windows
button = tk.Button(window, text="Open GIF Windows", command=main)
button.pack()

window.mainloop()
