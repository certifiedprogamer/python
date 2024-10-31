import csv
import random
import json


def get_dictionary_entry(list_of_keys, list_of_vals, main_list):
    """accepts two lists of matching key/value pairs.
    converts the key/value pairs to a dictionary and returns."""
    entry = {}
    for i in range(len(list_of_keys)):
        entry[list_of_keys[i]] = list_of_vals[i]
    return entry


def print_element_info(e):
    print(f"{e["Element"]} has an atomic number of {e["AtomicNumber"]} and a mass of "
          f"{e["AtomicMass"]}")


def play_game(element_list):
    """repeatedly chooses elements from the list and prompts the user to guess the element's symbol"""
    score = 0
    while True:
        rand_element_idx = random.randint(0, len(element_list) - 1)
        rand_element = element_list[rand_element_idx]
        response = input(f"Enter the symbol for {
                         rand_element["Element"]} or Q to quit: ").strip()
        if response.lower() == "q":
            break
        if response == rand_element["Symbol"]:
            print("You got it!")
            score += 1
        else:
            print(f"That's incorrect. The correct answer was {
                  rand_element["Symbol"]}")
        print(f"Current score: {score}")
        more = input(f"Would you like to know more about {
                     rand_element["Element"]}? (y/n)").lower().strip()
        if more == "y":
            print(json.dumps(rand_element, indent=4))


def lookup_element(element_list):
    symbol = input(f"Enter the element symbol to look up: ")
    element = find_element(element_list, symbol)
    print(json.dumps(element, indent=4))


def find_element(element_list, symbol):
    element = list(filter(lambda x: x["Symbol"] == symbol, element_list))
    if not element:
        return None
    else:
        return element[0]


def main():
    # load our csv into a list of dictionaries.
    element_list = []
    with open("periodic_table.csv", "r") as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        for line in csv_reader:
            entry = get_dictionary_entry(headings, line, element_list)
            element_list.append(entry)

        # print(json.dumps(element_list, indent=4))
        choice = input(
            "Enter p to play the symbol game, enter l to look up an element: :").strip().lower()
        if choice == "p":
            play_game(element_list)
        elif choice == "l":
            lookup_element(element_list)


if __name__ == "__main__":
    main()
