# dictionaries are data structures made of key/value pairs

point = {"x": 1, "y": 2, "creator": "Mosh", 5: "five"}
# alt syntax for dictionaries
point2 = dict(x=1, y=2)
print(point)
print(point2)

print(point["x"])
point["x"] = 5
print(point["x"])


point["r"] = ":("
print(point["r"])

# print(point["s"]) error very bad

# how to handle:

if "s" in point:
    print(point["s"])
else:
    print("yargh there be no s")

# delete a key/value from dictionary:
del point["creator"]

# cleaner approach
print(point.get("creator", "God is dead."))

# iterate through a dictionary
for key in point:
    print(f"{key} : {point[key]}")

print(point.items())
for key, value in point.items():
    print(f"{key}: {value}")
