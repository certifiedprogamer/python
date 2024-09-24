# write a function that prompts a user for 1 or 2
# if the user inputs anything else, report the error and ask again.

def one_or_two():
    while True:
        num = (input("Please enter 1 or 2: "))
        if num == "1" or num == "2":
            return num
        else:
            print("Error! only input 1 or 2.")


print(one_or_two())
