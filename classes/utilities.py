def say_hello(name="Jesse Catsopolous"):
    print(f"Hello {name}")


def get_lowest_num(*nums):
    """Takes any number of numbers and returns the minimum"""
    min = None
    for num in nums:
        if min == None or min > num:
            min = num
    return min


print("hi")
