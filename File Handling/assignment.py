# Kerry Sowers
import csv
try:
    with open('sales.csv', 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        total_sales = 0
        for row in csv_reader:
            try:
                total_sales += float(row[1]) * int(row[2])
            except ValueError:
                print("Incorrect data type detected.")
                print("Resuming function...")
        print(f"Total sales amount: ${total_sales:.2f}")
except FileNotFoundError:
    print("File doesn't exist.")

# user_in = input(
#    "what do you want to do? (enter \"add\" to add a new expense, enter \"view\" to view total expenses, and enter \"date\" to view all expenses for a specific date): ")
# user_in = user_in.lower()
# if user_in == "add":
#    with open("expenses.csv", "a", newline="") as file:
#        date = input("Enter date: ")
#        item = input("Enter item: ")
#        cost = input("Enter amount: ")
#        total = [date, item, cost]
#        writer = csv.writer(file)
#        writer.writerow(total)
# elif user_in == "view":
#    with open("expenses.csv", "r") as file:
#        total = 0
#        csv_reader = csv.reader(file)
#        headers = next(csv_reader)
#        for row in csv_reader:
#            total += float(row[2])
#        print(f"Total expenses: ${total}")
# elif user_in == "date":
#    with open("expenses.csv", "r") as file:
#        csv_reader = csv.reader(file)
#        date = input("Enter date: ")
#        print(f"Expenses on {date}")
#        for row in csv_reader:
#            if row[0] == date:
#                print(f"{row[1]}: {row[2]}")

    # with open('employees.csv', 'r') as file:
    #     csv_reader = csv.reader(file)
    #     for row in csv_reader:
    #         print(f"{row[0]} works in {row[2]}")

    # user_in = input(
    #     "what do you want to do? (enter \"add\" to add a task, enter \"view\" to view uncompleted tasks, and enter \"complete\" to mark a task as completed.)")
    # user_in = user_in.lower()
    # if user_in == "add":
    #     with open("tasks.txt", "a") as file:
    #         add = input("Enter task: ")
    #         file.write(f"{add}\n")
    # elif user_in == "view":
    #     with open("tasks.txt", "r") as file:
    #         print("Remaining tasks:")
    #         for row in file:
    #             print(row, end="")
    # elif user_in == "complete":
    #     with open("tasks.txt", "r") as file:
    #         old_file = file.read()
    #         print("Current file:")
    #         print(old_file)
    #     with open("tasks.txt", "w") as file:
    #         replace = input("enter the name of the task you want to replace.")
    #         new_file = old_file.replace(replace+"\n", "")
    #         file.write(new_file)

    # from datetime import date
    # import queue
    # while True:
    #    user_input = input("\n Enter a new diary entry or \"list\" to view all: ")
    #    current_date = date.today()
    #    if user_input == "list":
    #        with open("diary.txt", "r") as file:
    #            queue = []
    #            for row in file:
    #                queue.append(row)
    #            for i in range(len(queue)):
    #                print(queue.pop(0), end="")
    #    else:
    #        with open("diary.txt", "a") as file:
    #            file.write(f"{current_date}: {user_input}")

    # with open("guest_list.txt", "a") as file:
    #    guest = input("enter guest name: ")
    #    file.write(f"{guest} \n")

    # with open("guest_list.txt", "r") as file:
    #    count = 0
    #    for i in file:
    #        count += 1
    #    print(f"Guest added! Total guests: {count}")

    # with open("notes.txt", "w") as file:
    #    note = input("Enter a note:")
    #    file.write(note)
    #    print("Note saved!")
