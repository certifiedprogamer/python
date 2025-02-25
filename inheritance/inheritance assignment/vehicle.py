class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(
            f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, ", end="")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.doors}")


car = Car("Toyota", "Corolla", 2020, 4)
car.display_info()
