import math


class Point:

    default_color = "red"
    # Default constructor

    def __init__(self, x=10, y=15) -> None:
        self.x = x
        self.y = y

    # This is an instance method because it uses self and references instance variables (eg.self.x)
    def calculate_distance(self, another_point):
        xvals_squared = (another_point.x - self.x)**2
        yvals_squared = (another_point.y - self.y)**2
        distance = math.sqrt(xvals_squared+yvals_squared)
        return distance

    def draw(self):
        print(f"Point drawn at ({self.x}, {self.y})")

    # magic methods:

    # used when i print a point

    def __str__(self):
        return f"{self.x, self.y}"

    # used when i compare points with ==

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    # class methods are not called on instances of the class(objects)

    @classmethod
    def find_distance_between_points(cls, p1, p2):
        xvals_squared = (p2.x - p1.x)**2
        yvals_squared = (p2.y - p1.y)**2
        distance = math.sqrt(xvals_squared+yvals_squared)
        return distance

    # static methods are not called on instances of class objects.
    # a static method does not have access to class level variables.

    @staticmethod
    def find_the_distance_between_points(p1, p2):
        xvals_squared = (p2.x - p1.x)**2
        yvals_squared = (p2.y - p1.y)**2
        distance = math.sqrt(xvals_squared+yvals_squared)
        return distance
