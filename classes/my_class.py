class Student:

    def __init__(self, first="fgfg", last="b", gpa=0, scores=[0, 0, 0]):
        self.first = first
        self.last = last
        self.gpa = gpa
        self.scores = scores

    def say_hello(self):
        print(f"Hello, my name is {self.first} {
              self.last}, my gpa is {self.gpa}, my scores were {self.scores} ")

    def __str__(self):
        return f"{self.first} {self.last}"
