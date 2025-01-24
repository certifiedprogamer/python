class Car:

    def __init__(self, make=None, model=None, mpg=None):
        self.make = make
        self.model = model
        self.mpg = mpg

    def go(self):
        print(f"{self.make} {self.model} IS GO")
        print("BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRHBFBRHFBRKRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRCARNOISESBRBRBRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")

    def calculate_trip_cost(self, dist: float, gas_gallon_cost: float) -> float:
        cost = 0
        cost = self.gallons_needed(dist) * gas_gallon_cost
        return cost

    def gallons_needed(self, dist: float) -> float:
        return dist/self.mpg
