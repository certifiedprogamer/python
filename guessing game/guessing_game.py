import random
import time


def play_game():
    """Game loop"""
    number = random.randint(0, 100)
    typetext("I'm thinking of a number between 0 and 100. Can you guess it?")
    player_guess = 101
    computer_guess = (101, False)
    computer_guess_count = 0
    player_guess_count = 0
    while player_guess != number:
        player_guess = get_integer_input(number)
        player_guess_count += 1
    typetext(f"It took you {
             player_guess_count} guesses to guess the correct number.")
    typetext("Now, let me try to guess the number myself.")
    highest = 100
    lowest = 0
    while computer_guess[0] != number:
        computer_guess = computer_algorithm(number, highest, lowest)
        computer_guess_count += 1
        if computer_guess[1] == False:
            lowest = computer_guess[0]
        elif computer_guess[1] == True:
            highest = computer_guess[0]
    typetext(f"It took me {
             computer_guess_count} guesses to find the correct number.")
    typetext(f"It took you {
             player_guess_count} guesses to find the correct number.")
    if computer_guess_count < player_guess_count:
        typetext("I won!")
    elif player_guess_count < computer_guess_count:
        typetext("You won!")
    elif player_guess_count == computer_guess_count:
        typetext("It took us the same amount of tries.")


def typetext(str, end="\n"):
    """Makes text be typed out slower, allowing the user to follow along."""
    for character in str:
        print(character, end="", flush=True)
        time.sleep(.01)
    print(end, end="")


def get_integer_input(number):
    """Gets the user's input from 0 to 100"""
    while True:
        try:
            guess = int(input("Your guess:"))
            if guess == number:
                typetext("Correct!")
                return guess
            elif guess > number:
                typetext("Too high! Try again!")
                return guess
            elif guess < number:
                typetext("Too low! Try again!")
                return guess

        except:
            print("Guess was not a number. Try again.")


def computer_algorithm(number, highest, lowest):
    guess = (highest + lowest) // 2
    typetext(f"My guess: {guess}")
    if guess > number:
        typetext(f"The number is lower than {guess}")
        return guess, True
    elif guess < number:
        typetext(f"The number is higher than {guess}")
        return guess, False
    elif guess == number:
        typetext(f"I got it right!")
        return guess, False


if __name__ == "__main__":
    while True:
        play_game()
        typetext(
            "Would you like to play again? (type y or Y to say yes, type anything else to quit.)")
        play = input("")
        if play == "y" or play == "Y":
            typetext("Let's go.")
        else:
            typetext("Goodbye.")
