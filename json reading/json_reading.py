import json
# Write a program that will print all the ids and titles of the games.
# When a user inputs an id, we will print out the title, summary, and list of platforms it was available on.
# Do this until the user hits Q.


def load_data_from_file():
    """opens the file and loads the json. Returns a dictionary of the data"""
    with open("mario_games.json", "r") as file:
        data = json.load(file)
        return data


def display_game_listings(data):
    for entry in data.keys():
        print(f"{entry} : {data[entry]["name"]}")


def display_game_data(data, resp):
    """ print out the title, summary, and list of platofmrs it was available on."""
    print(data[resp]["name"])
    print(data[resp]["summary"])
    print(f"Platforms: {data[resp]["platform"]}")


def main():
    """Accepts input from user to determine what to do.
       Repeats until the user hits Q."""
    data = load_data_from_file()
    display_game_listings(data)
    while True:
        resp = input("Enter a game id or Q to quit: ").strip().lower()
        if resp == "q":
            break
        display_game_data(data, resp)
        # display game data


if __name__ == "__main__":
    main()
