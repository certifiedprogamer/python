class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 1:
            raise ValueError("Name length must be at least 2 characters")
        self.__name = name


p = Person("John")
print(p.name)
p.name = "A"
