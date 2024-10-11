# try to create a tuple of even numbers with comprehension
from sys import getsizeof
values = (f"id {x*2}" for x in range(600000))
values2 = [f"id {x*2}" for x in range(600000)]
# for v in values:
#     print(v)
#     break
# print(values)
print(f"Gen size: {getsizeof(values)}")
print(f"Lst size: {getsizeof(values2)}")
