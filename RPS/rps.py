import random


def player_input():
    """Gets input from the player"""
    while True:
        choice = input(
            "Enter 1 for rock, 2 for paper, or 3 for scissors: ").strip()
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)
        else:
            print("Invalid input. Try again.")


def computer_input():
    """Chooses between rock, paper, and scissors randomly."""
    choice = random.randint(1, 3)
    return choice


def round_end_compiler(player_choice, computer_choice, round):
    """Turns the results from the end of the round into a list to be added to end_list"""
    choice_bank = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You played {choice_bank[player_choice]}. The computer played {
          choice_bank[computer_choice]}.")
    outcome = outcome_check(player_choice, computer_choice)
    compiled = (round, choice_bank[player_choice],
                choice_bank[computer_choice], outcome)
    return compiled


def outcome_check(player_choice, computer_choice):
    """Determines the outcome of the last round."""
    if player_choice == 1 and computer_choice == 3:
        print("You win!")
        return "Win"
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
        return "Win"
    elif player_choice == 3 and computer_choice == 2:
        print("You win!")
        return "Win"
    elif computer_choice == 1 and player_choice == 3:
        print("You lost!")
        return "Lose"
    elif computer_choice == 2 and player_choice == 1:
        print("You lost!")
        return "Lose"
    elif computer_choice == 3 and player_choice == 2:
        print("You lost!")
        return "Lose"
    else:
        print("It's a tie!")
        return "Tie"


def percent_calculator(end_list):
    """Calculates the percentage of rounds won, lost, and tied."""
    win_percent = 0
    lose_percent = 0
    tie_percent = 0
    percent_increment = 100 / len(end_list)
    for i in end_list:
        if i[3] == "Win":
            win_percent += percent_increment
        elif i[3] == "Lose":
            lose_percent += percent_increment
        elif i[3] == "Tie":
            tie_percent += percent_increment
    return win_percent, lose_percent, tie_percent


def start_screen():
    """Prints out ASCII art for the start screen of the game."""
    print(".-. .-. .-. . .     .-. .-. .-. .-. .-.     .-. .-. .-. .-. .-. .-. .-. .-.")
    print(
        "|(  | | |   |<      |-' |-| |-' |-  |(      `-. |    |  `-. `-. | | |(  `-. ")
    print("' ' `-' `-' ' ` ,   '   ` ' '   `-' ' ' ,   `-' `-' `-' `-' `-' `-' ' ' `-'")
    print("    _______           _______               _______ ")
    print("---'   ____)      ---'   ____)____     ---'    ____)____ ")
    print("      (_____)               ______)               ______) ")
    print("      (_____)               _______)           __________)")
    print("      (____)               _______)           (____) ")
    print("---.__(___)       ---.__________)      ---.__(___)")
    print()


def end_screen(end_list):
    "Prints out a report showing what rounds were won, lost, and tied, along with the win and loss percentage. "
    print("##############################################################")
    print("################ Rock, Paper, Scissors Report ################")
    print("##############################################################")
    print("--------------------------------------------------------------")
    print("|  Round  |   User Played   |   Computer Played  |  Outcome  |")
    print("--------------------------------------------------------------")
    for i in end_list:
        print(f"|    {i[0]}    |{i[1].rjust(17, " ")}|{
              i[2].rjust(20, " ")}|{i[3].rjust(11, " ")}|")
        print("--------------------------------------------------------------")
    percent = percent_calculator(end_list)
    print(f"You won {percent[0]}% of the matches.")
    print(f"You lost {percent[1]}% of the matches.")
    print(f"You tied {percent[2]}% of the matches.")
    win_decider(percent)


def win_decider(percent):
    """Decides who won based off the percentage of wins."""
    if percent[0] > percent[1]:
        print("You won the series.")
    elif percent[1] > percent[0]:
        print("You lost the series.")
    else:
        print("The series is a tie.")


def game_loop():
    """The main loop the game takes place in."""
    start_screen()
    end_list = list()
    for round in range(1, 6):
        print(f"Round {round}")
        player_choice = player_input()
        computer_choice = computer_input()
        end_list.append(round_end_compiler(
            player_choice, computer_choice, round))
    end_screen(end_list)


if __name__ == "__main__":
    game_loop()
