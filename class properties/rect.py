class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = length * width

    @property
    def area(self):
        return self._area


rect = Rectangle(5, 4)
print(rect.area)
rect.area = 30
