from abc import ABC, abstractmethod


class Game(ABC):
    def play(self):
        print("im game beign played")

    @abstractmethod
    def print_stats(self):
        pass


class SwitchGame(Game):
    def print_stats(self):
        print("printing switch stats")


game = SwitchGame()

game.play()
game.print_stats()
