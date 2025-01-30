class Utilities:
    def determine_winner(player1, player2):
        """Determines the winner of the round"""
        if player1 == "Rock" and player2 == "Scissors":
            return 1
        elif player1 == "Paper" and player2 == "Rock":
            return 1
        elif player1 == "Scissors" and player2 == "Paper":
            return 1
        elif player2 == "Rock" and player1 == "Scissors":
            return -1
        elif player2 == "Paper" and player1 == "Rock":
            return -1
        elif player2 == "Scissors" and player1 == "Paper":
            return -1
        else:
            return 0

    def convert_to_play(p: str):
        """Converts r, p, and s into rock, paper, and scissors"""
        choice_bank = {"r": "Rock", "p": "Paper", "s": "Scissors"}
        try:
            play = choice_bank[p]
            return play
        except:
            return p


if __name__ == "__main__":
    play1 = "r"
    play1 = Utilities.convert_to_play(play1)
    play2 = "s"
    play2 = Utilities.convert_to_play(play2)
    wincheck = Utilities.determine_winner(play1, play2)
    print(play1)
    print(play2)
    print(wincheck)
