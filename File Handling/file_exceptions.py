import os
try:
    with open("garfield.txt") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("file not found")


# exceptions can be expensive

# check first to see if file exists
# filename = "C:\\Users\\CMP_KeSowers\\Desktop\\python\\File Handling"
filename = "garfield.txt"
if os.path.exists(filename):
    with open(filename) as file:
        content = file.read()
        print(content)
else:
    print("file doesn't exist")
