def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print("Start")
print(multiply(2, 3, 4, 5))
