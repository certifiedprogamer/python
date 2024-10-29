# Write a program that prints the letter than occurs the most in the string
# votes = list()
# while True:
#     candidate = input("Enter the name of a candidate (or *** to stop.):")
#     if candidate == "***":
#         break
#     votes.append(candidate)
# count = dict(c=0)
# for c in votes:
#     count[c] = 0
# for c in votes:
#     count[c] += 1
# highest = (0, 0)
# for c in votes:
#     if highest[0] > count[c]:
#         pass
#     elif highest[0] < count[c]:
#         highest = (count[c], c)

# majority_check = highest
# for c in votes:
#     if majority_check[0] == count[c]:
#         highest = (count[c], c)
#         if majority_check[1] != highest[1]:
#             print("Runoff!")
#             exit()
# print(highest[1])

# save for later
# n = int(input(""))
# m = int(input(""))
# p = m // n
# k = m / n
# z = p + 1
# print(p)
# print(k)
# k = k - p
# b = k
# g = 0
# while g != n:
#    if k >= 1:
#        print("*" * z)
#        k = b
#    else:
#        print("*" * p)
#    k += k
#    g += 1

g = input("")

g = list(enumerate(g))
print(g)
count = 0

for i in g:
    if i[1] == "-":
        min = i[0] - 1
        max = i[0] + 1
        print(min, max)
