from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14


shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())
