# a function with a variable number of arguments
def multiply(message, *numbers):
    product = 1
    print(f"{message} {numbers}")
    for num in numbers:
        product *= num
    return product


print(multiply("I'm multiplying", 2, 3, 4, 5))
