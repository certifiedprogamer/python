class Dog:
    def __init__(self, name: str, breed: str, age=1):
        self.name = name
        self.breed = breed
        self.age = age

    def birthday(self):
        self.age += 1


dog = Dog("Buddy", "Labrador")

print(dog.age)

dog.birthday()

print(dog.age)
