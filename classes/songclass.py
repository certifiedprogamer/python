class Song:
    def __init__(self, title: str, length_in_seconds: int, artist_name: str, bpm: int):
        self.title = title
        self.length = length_in_seconds
        self.artist = artist_name
        self.bpm = bpm

    def __str__(self):
        return f"{self.title, self.length, self.artist, self.bpm}"

    def beat_calculator(self):
        x = self.length / 60
        print(x)
        return f"Total beats: {x * self.bpm}"
