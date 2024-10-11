acronym_dictionary = {"LOL": "Laugh out loud", "AFK": "Away from keyboard", "BRB":
                      "Be right back", "TYSM": "Thank you so much",
                      "TTYL": "Talk to you later"}

while True:
    acronym = input("Enter an acronym (or Q to quit): ")
    if acronym in acronym_dictionary:
        print(acronym_dictionary[acronym])
    elif acronym == "q" or acronym == "Q":
        print("bye bye")
        break
    else:
        print(f"{acronym} is not in the dictionary.")
        add_acronym = input("Would you like to add it? (yes/no):")
        if add_acronym == "yes":
            new_acronym = input(f"Enter the meaning for {acronym}: ")
            acronym_dictionary[acronym] = new_acronym
            print(f"{acronym} has been added to the dictionary.")
        else:
            print("Nevermind.")
    print("")
