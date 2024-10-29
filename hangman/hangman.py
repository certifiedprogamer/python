# Kerry Sowers
import random

def word_bank():
    animals = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
    python = ["integer", "function", "boolean",
             "float", "string", "dictionary", "lambda", "loop",
             "debug", "scope"]
    geometry = ["square", "triangle", "rhombus", "line", "segment", "angle", "area", "parallel"]
    while True:
        choice = input("Pick a word bank from which I will choose one. (python, geometry, animals.)")
        


def hangman_initialize():
    """Chooses a word from the list for the player to guess."""
    words = ["integer", "function", "boolean",
             "float", "string", "dictionary", "lambda", "loop",
             "debug", "scope"]
    chosen_word = random.choice(words)
    return chosen_word


def guess_initialize(word):
    """Initialize the list the player will use to guess the word."""
    guess = list(word)
    i = 0
    for l in word:
        guess[i] = '_'
        i += 1
    return guess


def word_guess(word, unknown, incorrect_letters):
    """Take input from the player and see if it matches with a letter in the word."""
    print(f"Incorrect guesses: {incorrect_letters}")
    print(f"Word: {unknown}")
    guess = "filler text"

    while len(guess) != 1:
        guess = str(input("guess a letter in the word: "))
        if len(guess) > 1:
            print("Only one letter allowed.")
        elif guess in incorrect_letters or guess in unknown:
            print("You already guessed that.")
            guess = "filler text"

    guess = guess.strip()
    guess = guess.lower()

    if guess in word:
        g = list(enumerate(word))
        for l in g:
            if l[1] == guess:
                unknown[l[0]] = l[1]
        return unknown, True
    else:
        return guess, False


def hangman_picture(wrong_guess_count):
    """Create a picture of the current hangman using HANGMANPICS"""
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
    print(HANGMANPICS[wrong_guess_count])


def win_check(unknown, word, wrong_guess_count):
    """Checks if the player has won, lost, or if the game is still going."""
    if wrong_guess_count >= 6:
        return "You lose!", False
    for i in unknown:
        if i not in word:
            return 0, "no"
    else:
        return "You win!", True


def game_loop():
    """The main loop in which the game takes place"""
    word = hangman_initialize()
    unknown = guess_initialize(word)
    incorrect_letters = list()
    wrong_guess_count = 0
    guess_count = 0
    while True:
        hangman_picture(wrong_guess_count)
        check = win_check(unknown, word, wrong_guess_count)
        if check[1] == False:
            print(unknown)
            print(f"{check[0]} The word was {word}.")
            break
        elif check[1] == True:
            print(unknown)
            print(f"{check[0]}")
            print(f"It took you {guess_count} guesses")
            break
        guess = word_guess(word, unknown, incorrect_letters)
        guess_count += 1
        if guess[1] == True:
            unknown = guess[0]
        elif guess[1] == False:
            incorrect_letters.append(guess[0])
            wrong_guess_count += 1


if __name__ == "__main__":
    play = input("Would you like to play a game? (Y/N)")
    while play == "Y" or play == "y":
        game_loop()
        play = input("Would you like to play again? (Y/N)")
    print("Goodbye.")
