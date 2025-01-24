class Player:
    def __init__(self, player: list):
        self.name = player[0]
        self.plays = player[1:]
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.series_wins = 0
        self.score = 0.0

    def calculate_score(self):
        self.score = self.wins + (self.ties / 2)

    def __str__(self):
        return f"{self.name}: plays: {self.plays} wins: {self.wins} losses: {self.losses} ties: {self.ties} score: {self.score} series wins: {self.series_wins}"


if __name__ == "__main__":
    player = Player(['Joe', 's', 'r', 'r', 'p', 's'])
    player.wins = 4
    player.ties = 2
    player.calculate_score()
    print(player)
