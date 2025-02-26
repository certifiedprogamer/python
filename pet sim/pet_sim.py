from abc import ABC, abstractmethod
import time
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
        time.sleep(1)
        print(f"{self.name} eats some food.")
        print("-20 hunger.")
        print("+10 energy.")
        time.sleep(1)
        self.hunger -= 20
        self.energy += 10

    def play(self):
        time.sleep(1)
        print(f"{self.name} plays with you!")
        print("+15 happiness.")
        print("-10 energy.")
        time.sleep(1)
        self.happiness += 15
        self.energy -= 10

    def sleep(self):
        time.sleep(1)
        print(f"{self.name} takes a nap.")
        print("+20 energy.")
        print("+10 hunger.")
        time.sleep(1)
        self.energy += 20
        self.hunger += 10

    def show_status(self):
        time.sleep(1)
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")
        time.sleep(1)

    def random_event_handler(self):
        rand_choice = randint(1, 10)
        if rand_choice == 1 or rand_choice == 2 or rand_choice == 3:
            # event
            return True
        else:
            return False

    def random_event(self):
        if self.random_event_handler():
            rand = randint(1, 4)
            time.sleep(1)
            if rand == 1:
                print(f"{self.name} found a snack!")
                print("-10 hunger.")
                self.hunger -= 10
            elif rand == 2:
                print(f"{self.name} plays alone.")
                print("+10 happiness.")
                self.happiness += 10
            elif rand == 3:
                print(f"{self.name} had a bad dream.")
                print("-10 energy.")
                self.energy -= 10
            elif rand == 4:
                print(f"{self.name} found a toy!")
                print("+10 happiness.")
                self.happiness += 10
            time.sleep(1)
        else:
            pass

    @abstractmethod
    def special_ability(self):
        pass


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def play(self):
        time.sleep(1)
        print(f"{self.name} plays with you!")
        print("+20 happiness.")
        print("-10 energy.")
        time.sleep(1)
        self.happiness += 20
        self.energy -= 10

    def special_ability(self):
        time.sleep(1)
        print("Loyal Companion: ")
        if self.happiness >= 80:
            print(f"{self.name} is excited and forgets to eat!")
            print("Hunger reduced by 10!")
            self.hunger -= 10
        else:
            print("Not enough happiness to perform ability.")
        time.sleep(1)


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def sleep(self):
        time.sleep(1)
        print(f"{self.name} takes a nap.")
        print("+30 energy.")
        print("+5 hunger.")
        time.sleep(1)
        self.energy += 30
        self.hunger += 5

    def special_ability(self):
        time.sleep(1)
        print("Independent Napper: ")
        if self.energy <= 20:
            print(f"{self.name} sleeps on its own.")
            print("Energy increased by 15!")
            self.energy += 15
        else:
            print("Energy isn't low enough to perform ability.")
        time.sleep(1)


class Dragon(Pet):
    def __init__(self, name):
        super().__init__(name)

    def feed(self):
        time.sleep(1)
        print(f"{self.name} eats some food.")
        print("-30 hunger.")
        print("+15 energy.")
        print("+10 happiness.")
        time.sleep(1)
        self.hunger -= 30
        self.energy += 15
        self.happiness += 10

    def play(self):
        time.sleep(1)
        print(f"{self.name} plays with you!")
        print("+25 happiness.")
        print("+10 hunger.")
        print("-10 energy.")
        time.sleep(1)
        self.happiness += 25
        self.hunger += 10
        self.energy -= 15

    def special_ability(self):
        time.sleep(1)
        print("Fiery Roar: ")
        if self.happiness >= 70:
            print(f"{self.name} is excited from roaring!")
            print("Hunger reduced by 5!")
            print("Energy increased by 5!")
            self.hunger -= 5
            self.energy += 5
        else:
            print("Not enough happiness to perform ability.")
        time.sleep(1)


def pet_sim():
    name = input("Enter the name of your pet: ")
    while True:
        time.sleep(1)
        try:
            pet_type = int(input(
                "Select your pet type (numbers only): \n 1. Dog 🐶 \n 2. Cat 🐱 \n 3. Dragon 🐉 \n "))
            if pet_type == 1 or pet_type == 2 or pet_type == 3:
                break
            else:
                time.sleep(1)
                print("That is not one of the options. Try again.")
        except:
            time.sleep(1)
            print("That is not one of the options. Try again.")
    if pet_type == 1:
        p = Dog(name)
    elif pet_type == 2:
        p = Cat(name)
    elif pet_type == 3:
        p = Dragon(name)
    while True:
        time.sleep(1)
        p.show_status()
        time.sleep(1)
        while True:
            try:
                action = int(input(
                    "Choose an action: \n 1. Feed \n 2. Play \n 3. Sleep \n 4. Use Special Ability \n 5. Exit \n"))
                if action == 1 or action == 2 or action == 3 or action == 4 or action == 5:
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    print("That is not a valid action. Try again.")
            except:
                time.sleep(1)
                print("That is not a valid action. Try again.")
                time.sleep(1)
        if action == 1:
            p.feed()
            p.random_event()
        elif action == 2:
            p.play()
            p.random_event()
        elif action == 3:
            p.sleep()
            p.random_event()
        elif action == 4:
            p.special_ability()
            p.random_event()
        elif action == 5:
            print("Goodbye.")
            exit()


if __name__ == "__main__":
    pet_sim()
