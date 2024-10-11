# make a list of even numbers:
values = []
for x in range(6):
    values.append(x * 2)
print(values)

# same thing, but with comprehension
values = [x * 2 for x in range(6)]
print(values)

values = {}
for x in range(6):
    values[x] = x*2

print(values)

# comprehension style:
values = {x: x * 2 for x in range(6)}
print(values)
