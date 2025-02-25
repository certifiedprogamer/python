class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        print(f"{self.name} is a {self.species}")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def describe(self):
        super().describe()
        print(f"Breed: {self.breed}")

    # def describe(self):
        # print(f"{self.name} is a {self.species} of breed {self.breed}")


dog = Dog("Buddy", "Dog", "Labrador")
dog.describe()
