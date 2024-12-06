from tkinter import *
from PIL import ImageTk
from PIL import Image as I
import requests
from io import BytesIO
import json

from tkinter import *


class WebImage:
    def __init__(self, url, width, height):
        u = requests.get(url)

        self.image = ImageTk.PhotoImage(
            I.open(BytesIO(u.content)).resize((width, height)))

    def get(self):
        return self.image


root = Tk()
root.title("Puppies")
search_terms = "bear"
x = requests.get(
    f'https://api.pexels.com/v1/search?query={search_terms}&per_page=80', headers={"Authorization": "563492ad6f91700001000001a54be4455d7048a681f1cbe4609601fa"})
# print(x.json())
resp = x.json()

print(json.dumps(resp, indent=4))

link = resp["photos"][0]["src"]["original"]
orig_width = resp["photos"][0]["width"]
orig_height = resp["photos"][0]["height"]

width = 100
ratio = orig_width/width
height = int(orig_height//ratio)

img = WebImage(link, width, height).get()
imagelab = Label(root, image=img)
imagelab.grid(row=0, column=0)

root.mainloop()


# print(resp["photos"][0]["src"]["original"])

# frame2 = PhotoImage(file=x.data, format="gif -index 2")
