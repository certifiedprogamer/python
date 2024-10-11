# Write a program that prints the letter than occurs the most in the string
sentence = "this is a common interview question"
count = dict(c=0)
for c in sentence:
    count[c] = 0
for c in sentence:
    count[c] += 1
highest = (0, 2)
for c in sentence:
    if highest[0] > count[c]:
        pass
    elif highest[0] < count[c]:
        highest = (count[c], c)


print(count)
print(highest)
