while True:
    user_input = input("1 or 2: ").strip()
    if user_input in ["1", "2"]:
        print("thank you")
        break
    else:
        print("invalid")
print(user_input)


num = 100
while num > 0:
    print(num)
    num -= 1
