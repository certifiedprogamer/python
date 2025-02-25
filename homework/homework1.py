
# assign 10
cost = float(input("Enter the cost of your meal: "))
tip_percent = float(input("Enter the tip percentage you want to give: "))
tip_percent /= 100
if tip_percent == 0:
    print("No.")
else:
    tip = cost * tip_percent
    print(f"Tip: ${tip}")


# assign 9
# grocery_list = list()
# for i in range(3):
#     grocery = input("Enter a grocery item: ")
#     grocery_list.append(grocery)
# print(grocery_list)

# assign 8
# name = input("Enter your name: ")
# num = int(input("Enter a number: "))
# for i in range(num):
#    print(name)


# assign 7
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#    print("even")
# else:
#    print("odd")

# assign 6
# password = input("Enter a password: ")
# if len(password) < 8:
#    print("Weak password")
# else:
#    print("Strong password")

# assign 5
# item_price = float(input("Enter the price of your item: "))
# discount = abs(item_price * 0.15 - item_price)
# print(f"Total price after discount: {discount}")


# assign 4
# days = int(input("How many days has your book been overdue?: "))
# overdue_fine = days * 0.25
# print(f"Your total fine is ${overdue_fine}")

# assign 3
# age = int(input("Enter your age:"))
# if age <= 12:
#    tickets = 5
# elif age > 12 and age < 60:
#    tickets = 10
# elif age >= 60:
#    tickets = 7
# print(f"Tickets are ${tickets}")


# assign 2
# f_name = input("Please enter your first name: ")
# l_name = input("Please enter your last name: ")
# print(f"{f_name.upper()}, {l_name.upper()}")


# assign 1
# temp = float(input("Please enter today's temperature (Celsius): "))
# temp = temp * 1.8 + 32
# print(f"Today's temperature is {temp} degrees Fahrenheit")
