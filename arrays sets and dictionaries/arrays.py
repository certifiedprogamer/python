from array import array

numbers = array("I", [1, 2, 3, 4, 5])


numbers.append(6)
numbers[2] = 99
# numbers[3] = "g"
print(numbers)
print(numbers[2])
