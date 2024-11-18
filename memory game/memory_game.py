import time
import random
import os
import json


def get_name():
    """Gets the player's name"""
    print("Welcome to the Number Memory Game!")
    name = input("Enter your name:").strip()
    return name


def get_high_scores():
    """Fetches the current high score board"""
    with open("high_scores.json", "r") as data:
        high_scores = json.load(data)
    return high_scores


def print_high_scores(high_scores):
    """Prints the current high scores."""
    print("High scores:")
    for i in range(0, len(high_scores)):
        print(f"{i + 1}. {high_scores[i]["name"]} - {high_scores[i]["score"]}")


def player_response():
    """Gets the player's response"""
    while True:
        start_time = time.time()
        resp = input("Enter the numbers you just saw:")
        try:
            resp = int(resp)
            resp_time = int(time.time()) - int(start_time)
            return resp, resp_time
        except:
            print("Response included a letter. try again.")


def append_score(name, current_score, high_scores):
    """Appends the player's score to the scoreboard if it is higher than the others."""
    if current_score > high_scores[0]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[1]["score"]:
        high_scores.insert(1, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[2]["score"]:
        high_scores.insert(2, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[3]["score"]:
        high_scores.insert(3, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[4]["score"]:
        high_scores.insert(4, {"name": name, "score": current_score})
        high_scores.pop()
    with open("high_scores.json", "w") as f:
        json.dump(high_scores, f, indent=4)
    return high_scores


def game_loop(start_num, current_score, rounds, name, high_scores):
    """Main loop the game takes place in"""
    while True:
        rounds += 1
        rand_num = random.randint(start_num[0], start_num[1])
        start_num[0] *= 10
        start_num[1] *= 10
        print(f"Remember the following numbers: {rand_num}")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        resp = player_response()
        if resp[0] == rand_num:
            current_score += 100 // resp[1]
            print(f"Good job! - Current score: {current_score}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Too bad!")
            end_game(name, current_score, rounds, high_scores)
            break


def main():
    """Initializes the game."""
    name = get_name()
    high_scores = get_high_scores()
    print_high_scores(high_scores)
    start = input(
        "Press Enter to start the game or 'q' to quit: ").lower().strip()
    play = "y"
    if start == "q":
        quit()
    while play == "y":
        start_num = [100, 999]
        current_score = 0
        rounds = 0
        game_loop(start_num, current_score, rounds, name, high_scores)
        high_scores = get_high_scores()
        play = input("Would you like to play again? (y/n)").lower().strip()


def end_game(name, current_score, rounds, high_scores):
    """Prints the end screen and updates the high scores"""
    print(f"You completed {
          rounds} rounds with a final score of {current_score}")
    high_scores = append_score(name, current_score, high_scores)
    print("Updated high scores: ")
    print_high_scores(high_scores)


if __name__ == "__main__":
    main()
