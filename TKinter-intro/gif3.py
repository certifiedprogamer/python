import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random
import requests
from io import BytesIO
import json
# Define the Tenor API key and endpoint
API_KEY = "AIzaSyDfIGq3-lVlhGsQvEvQhYddB2EMraQ7Uz4"
# "https://g.tenor.com/v1/search"
BASE_URL = "https://tenor.googleapis.com/v2/search"


class GIFPlayer(tk.Label):
    frames = {}  # Store frames globally for each GIF

    def __init__(self, master, gif_url):
        super().__init__(master)

        # Store frames globally for reuse, using the URL as a key
        if gif_url not in GIFPlayer.frames:
            # Download the GIF from the URL
            response = requests.get(gif_url)

            # Convert the response content into a format that PIL can handle
            # Use BytesIO to read the content into an image
            img = Image.open(BytesIO(response.content))
            GIFPlayer.frames[gif_url] = [ImageTk.PhotoImage(
                img) for img in ImageSequence.Iterator(img)]

        self.frames = GIFPlayer.frames[gif_url]
        self.current_frame = 0
        self.update_frame()

    def update_frame(self):
        # Update the image with the next frame
        self.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(100, self.update_frame)  # Adjust the delay as needed


def get_gifs(query, limit=10):
    """
    Fetch GIFs from Tenor API based on a search query.
    Returns a list of URLs to GIFs.
    """

    # https://tenor.googleapis.com/v2/search?q=garfield&key=AIzaSyDfIGq3-lVlhGsQvEvQhYddB2EMraQ7Uz4&limit=50&client_key=garfield
    params = {
        "q": query,
        "key": API_KEY,
        "limit": limit,
    }
    response = requests.get(BASE_URL, params=params)

    # Check if the response is successful
    if response.status_code != 200:
        print(f"Error: Unable to fetch data (status code {
              response.status_code})")
        return []

    # Parse the JSON response
    data = response.json()

    # Debug: print the raw response to understand its structure
    print("API Response:", data)  # Remove this line in production code

    # Check if 'results' exists in the response
    if 'results' not in data:
        print("Error: 'results' not found in API response")
        return []

    # Extract gif URLs from the API response
    gif_urls = [item['media_formats']['gif']['url']
                for item in data['results']]

    return gif_urls


def main():
    # Get a list of GIFs from Tenor API
    gifs = get_gifs("garfield", limit=20)  # Change the search query as needed

    # Limit the number of windows to a reasonable number (e.g., 50)
    for i in range(50):
        top = tk.Toplevel(window)
        rand1 = random.randint(-1000, 1000)
        rand2 = random.randint(-1000, 1000)
        top.geometry("300x150")

        # Randomly select a GIF URL for each window
        gif_url = random.choice(gifs) if gifs else ""

        if gif_url:  # Only create the player if a valid URL is available
            x = window.winfo_x()
            y = window.winfo_y()

            # Create the GIF player with the selected GIF URL
            gif_player = GIFPlayer(top, gif_url)
            gif_player.pack()

            top.geometry("+%d+%d" % (x+rand1, y+rand2))
            top.wm_transient()
        else:
            print("No valid GIFs available.")


window = tk.Tk()
window.title("GIF Player")


# Button to trigger creation of random GIF windows
button = tk.Button(window, text="Open GIF Windows", command=main)
button.pack()

window.mainloop()


# set the apikey and limit the # coming back
apikey = "AIzaSyDfIGq3-lVlhGsQvEvQhYddB2EMraQ7Uz4"   # click to set to your apikey
ckey = "my_test_app"  # set the client_key for the integration
lmt = 5

# partial search
search = "smile"

r = requests.get(
    "https://tenor.googleapis.com/v2/search_suggestions?key=%s&client_key=%s&q=%s&limit=%s" % (apikey, ckey, search, lmt))

if r.status_code == 200:
    # return the search suggestions
    search_suggestion_list = json.loads(r.content)["results"]
    print(search_suggestion_list)
else:
    # handle a possible error
    search_suggestion_list = []
