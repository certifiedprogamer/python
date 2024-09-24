import math
my_int = 2
my_other_int = 14
print("MATHS!!!!!!!!!!!!!!!!!!!!!!")
print("Addition: 5 + 6 = ", + 5 + 6)
print(f"Addition: 5 + 6 = {5 + 6}")
print(f"Value of my_int: {my_int}")
print(f"Value of my_other_int: {my_other_int}")
sum = my_int + my_other_int
print(f"{my_int} + {my_other_int} = {sum}")
difference = my_other_int - my_int
print(f"{my_other_int} - {my_int} = {difference}")
product = my_int * my_other_int
print(f"{my_int} x {my_other_int} = {product}")
quotient = my_other_int / my_int
print(f"{my_other_int} / {my_int} = {quotient}")
remainder = my_other_int % my_int
print(f"{my_other_int} % {my_int} = {remainder}")
int_div_quotient = my_other_int // my_int
print(f"{my_other_int} // {my_int} = {int_div_quotient}")
power_result = my_other_int ** my_int
print(f"{my_other_int} ** {my_int} = {power_result}")


print(type(sum))
print(type(difference))
print(type(product))
print(type(quotient))

my_int += 5
print(my_int)

print(f"5.7 rounded: {round(5.7)}")
print(f"5.2 rounded: {round(5.2)}")
print(f"Absolute value of -12.3: {abs(-12.3)}")
print(f"The ceiling of 14.2 : {math.ceil(14.2)}")
print(f"The floor of 14.8 : {math.floor(14.2)}")
