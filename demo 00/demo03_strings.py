my_name = "Kerry Sowers"
length_of_my_name = len(my_name)
print(length_of_my_name)
print("First letter: " + my_name[0])
print("third letter: " + my_name[2])

first_name = my_name[0:5]
print(first_name)
last_name = my_name[6:]
print(last_name)

print('\nMore String Methods')
print("My name in upper case: " + my_name.upper())
print("My name in lower case: " + my_name.lower())
my_name = my_name.lower()
print(my_name)
print(my_name.title())
long_messy_string = "                        AAAAAAAAAAA                             "
print(long_messy_string.lstrip())

print(my_name.replace("kerry", "chad"))
print(my_name.replace("s", "😢", 1))
print(my_name.find("s"))
print("sow" in my_name)
