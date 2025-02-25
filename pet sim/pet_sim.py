from abc import ABC, abstractmethod
from random import *


class Pet(ABC):
    def __init__(self, name: str):
        self._hunger = 50
        self._happiness = 50
        self._energy = 50
        self.name = name

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if value < 0:
            self._hunger = 0
        elif value > 100:
            self._hunger = 100
        else:
            self._hunger = value

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if value < 0:
            self._happiness = 0
        elif value > 100:
            self._happiness = 100
        else:
            self._happiness = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            self._energy = 0
        elif value > 100:
            self._energy = 100
        else:
            self._energy = value

    def feed(self):
        self.hunger -= 20
        self.energy += 10

    def play(self):
        self.happiness += 15
        self.energy -= 10

    def sleep(self):
        self.energy += 20
        self.hunger += 10

    def show_status(self):
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

    def random_event_handler(self):
        rand_choice = randint(1, 10)
        for i in range(3):
            rand = randint(1, 10)
            if rand_choice == rand:
                # event
                return True
        else:
            return False

    def random_event(self):
        if self.random_event_handler():
            print("yea")
        else:
            pass


p = Pet("the j")

p.random_event()
