class Animal:

    def __init__(self, weight=5):
        self.weight = weight

    def eat(self):
        print("eat.")


class Mammal(Animal):
    def __init__(self, hc="brown", weight: float = 32):
        super().__init__(weight)
        self.hair_color = hc

    def walk(self):
        print("walk")


class Fish(Animal):

    def __init__(self, weight: int):
        super().__init__(weight)

    def swim(self):
        print("swim")

    # method overriding

    def eat(self):
        super().eat()
        print("glgugkgluglguglgugglguglguglug")


# multi level inheritance can get messy very fast.
class Horse(Mammal):
    def how_hungry(self):
        print("How hungry.......")


class Shark(Fish):
    def eat_meat(self, meat: Animal):
        # this is polymorphism
        if isinstance(meat, Horse):
            print("I'm so hungry I could eat a horse")
        print(f"I just ate a {meat.weight} pound animal.")


m = Mammal(weight=300)
f = Fish(2000)
m.eat()
m.walk()
print(m.weight)


f.eat()
f.swim()
print(f.weight)

h = Horse()
h.eat()
h.how_hungry()
print(h.weight)

s = Shark(weight=300)
print(s.weight)
s.eat_meat(h)
