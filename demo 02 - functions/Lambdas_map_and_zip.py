# Kerry Sowers

history = []
while True:
    action = input("Enter action: ")
    if "visit" in action:
        action = action.replace("visit", "Visited")
        print(f"{action}")
        action = action.removeprefix("Visited ")
        history.append(action)
        print(f"Current history: {history}")
        print("")
    elif "back" in action:
        back = history.pop(-2)
        print(f"Back to: {back}")
        print(f"Current history: {history}")
        print("")
    else:
        print("Unrecognized action.")


# from collections import deque
# queue = deque(["Customer1", "Customer2", "Customer3", "Customer4"])

# while queue:
#     serving = queue.popleft()
#     print(f"Now serving: {serving}")


# colors = ['red', 'blue', 'green']
# shapes = ['circle', 'square']


# colored_shapes = []
# for i in colors:
#     for n in shapes:
#         colored_shapes.append(f"{i} {n}")

# print(colored_shapes)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def even_filter(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False


# even_numbers = filter(even_filter, numbers)
# print(list(even_numbers))

# students = ['Alice', 'Bob', 'Charlie']
# grades = [85, 92, 78]

# student_grades = list(zip(students, grades))
# print(student_grades)


# coordinates = [(1, 2), (3, 4), (5, 6)]


# def coordinate_swapper(x):
#     x = list(x)
#     x.reverse()
#     return tuple(x)


# swapped_coordinates = map(coordinate_swapper, coordinates)
# print(list(swapped_coordinates))


# def expensive_product_filter(x):
#     if x[1] > 500:
#         return True
#     else:
#         return False


# products = [('Laptop', 1200), ('Phone', 800),
#             ('Tablet', 300), ('Monitor', 150)]

# expensive_products = filter(expensive_product_filter, products)

# print(list(expensive_products))


# def price_remover(x):
#     return x[0]


# product = map(price_remover, products)
# print(list(product))


# sorted_products = sorted(products, key=lambda x: x[1])

# print(sorted_products)
