class Point:

    # Default constructor
    def __init__(self) -> None:
        self.x = 10
        self.y = 15

    def draw(self):
        print(f"Point drawn at ({self.x}, {self.y})")
