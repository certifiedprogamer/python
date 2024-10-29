import csv

with open('sales.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # consumes/skips the first row because it's a header and puts it in a separate variable
    headers = next(csv_reader)
    for row in csv_reader:
        for i in range(len(headers)):
            print(f"{headers[i]}: {row[i]} ", end="")
        print()

# using the csv and the code above, create a list of dictionaries, where
# each dictionary is a character with the keys being the headings.


# lis = []
# with open("characters.csv", "r") as file:
#    csv_reader = csv.reader(file)
#    headers = next(csv_reader)
#    for row in csv_reader:
#        record = {}
#        for i in range(len(headers)):
#            record[headers[i].lower()] = row[i]
#        lis.append(record)
# print(lis)

# print(lis[0]["name"])


def get_garfield_characters():
    lis = []
    with open("characters.csv", "r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            record = {}
            for i in range(len(headers)):
                record[headers[i].lower()] = row[i]
            lis.append(record)
    return lis


def print_character_info(characters, idx):
    if 0 <= idx < len(characters):
        character = characters[idx]
        print(f"{character["name"]} is a {character["species"]} that is {
              character["age"]} years old and weighs {character["weight"]} pounds")


def main():
    characters = get_garfield_characters()
    idx = 2
    characters[idx]["weight"] = 15
    print_character_info(characters, idx)
    # print(characters)


if __name__ == "__main__":
    main()
