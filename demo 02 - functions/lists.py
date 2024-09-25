# lists are a data structure that contain an ordered list of elements.
# order means they can be accessed by an index.

# use square brackets for lists
games = ["Rocket League",
         "Titan Fall 2",
         "Rainbow 6: Siege",
         "Halo 3",
         "Keanu's Blackjack",
         "Terraria",
         "You don't wanna see me infuriated",
         "Mario Kart (SNES)"
         ]
high_scores = [2, 7, 5, 9]
mixed_list = ["Mr. Klins", 43, True]
list_of_lists = [
    ["Titan Fall 2", 7],
    ["Rocket League", 2],
    ["Halo 3", 9]
]
print(games[0])
print(games[2])
print(games[-1])

# changing values in a list:
games[-1] = "Garfield Kart"

print(games)


# slicing lists:
# a slice is a subset of a list
first_four = games[:4]  # Same as 0:4
print(first_four)

last_four = games[-4:]
print(last_four)

middle_slice = games[4:6]
print(middle_slice)


# Create a list of numbers:

numbers = list(range(10))
print(numbers)
# print every other element
print(numbers[::2])
print(numbers[1:7:2])

# reverse a list
print(numbers[::-1])

# combining lists
combine = games + high_scores
print(combine)

# Repeating lists

repeat = [5] * 10
print(repeat)

duplicated_score = high_scores * 2
print(duplicated_score)

# find the length of a list
print(len(high_scores))
print(len(duplicated_score))

# unpacking a list:

name, age, likes_teaching = mixed_list
print(f"{name} {age} {likes_teaching}")

# unpacking with remainder * (first, middle_chunk, last)
game1, *other_games, game2 = games
print(game1)
print(other_games)
print(game2)

# iterate through a list
for i in games:
    print(i)

# iterate through a list, but also know the index (use enumerate)
for index, game in enumerate(games):
    print(f"{index}: {game}")


# adding items to a list
# using the append method

games.append("Odie roleplay")
print(games)

# using the insert method

games.insert(1, "John Arbuckle's night on the town")
print(games)

# removing elements:

games.remove("Halo 3")
print(games)

# remove the last element

games.pop()
print(games)

# remove at specific index
games.pop(3)
print(games)

# find the index of an element
print(games.index("John Arbuckle's night on the town"))
# note: index is case sensitive, meaning you'll get an error if the element isnt exact or doesnt exist
# example: print(games.index("Odie roleplay"))

# to avoid value error:
if "Odie roleplay" in games:
    print(games.index("Odie roleplay"))
else:
    print("LOOK WHAT YOU DID")

# sorting lists
nums_to_sort = [6, 4, 5, 1, 9]
print(nums_to_sort)
nums_to_sort.sort()  # sorting in place - updating order of current list
print(nums_to_sort)
# sort can be reversed
nums_to_sort.sort(reverse=True)
# nums_to_sort.reverse can also be used instead.
print(nums_to_sort)

# create a new sorted list without editing the existing one:
new_nums_to_sort = sorted(nums_to_sort)
print(nums_to_sort)  # should be in reverse order
print(new_nums_to_sort)  # should be sourted
