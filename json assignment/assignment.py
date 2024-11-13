import json
# Kerry Sowers
with open("presidents.json", "r") as file:
    data = json.load(file)
resp = input("Enter the name of a president: ").strip().lower()
found = False
for i in range(0, len(data["presidents"])):
    if resp == data["presidents"][i]["name"].lower():
        age = data["presidents"][i]["birth_year"] - \
            data["presidents"][i]["term"]["start_year"]
        age *= -1
        print(f"{data["presidents"][i]["name"]} was {
              age} when he started his first term.")
        found = True
if found == False:
    print(f"{resp.title()} was not found in the data")


# 5
# print("Presidents with multiple vice presidents:")
# for i in range(0, len(data["presidents"])):
#    count = 1
#    for c in data["presidents"][i]["vice_president"]:
#        if c == ",":
#            count += 1
#        if count >= 2:
#            print(data["presidents"][i]["name"])
#            break

# 4
# print("Enter the starting year and end year in the time range of the presidents you want to look for below:")
# start = "g"
# end = "g"
# while True:
#     start = input("Start year: ")
#     end = input("End year:")
#     try:
#         start = int(start)
#         end = int(end)
#         break
#     except:
#         print("Either start year or end year were not correct years. Try again.")
# found = False
# for i in range(0, len(data["presidents"])):
#     if start <= data["presidents"][i]["term"]["start_year"] and end >= data["presidents"][i]["term"]["end_year"]:
#         print(f"{data["presidents"][i]["name"]}:  {
#               data["presidents"][i]["term"]["start_year"]} - {data["presidents"][i]["term"]["end_year"]}")
#         found = True
# if found == False:
#     print(f"No presidents were found between {start} and {end}")

# 3
# found = False
# for i in range(0, len(data["presidents"])):
#    if resp == data["presidents"][i]["party"].lower():
#        print(data["presidents"][i]["name"])
#        found = True
# if found == False:
#    print(f"No presidents from {resp} were found.")

# 2
# for i in range(0, len(data["presidents"])):
#     if resp == data["presidents"][i]["name"].lower():
#         print(f"{data["presidents"][i]["name"]} was a part of the {
#               data["presidents"][i]["party"]} party, and served from {data["presidents"][i]["term"]["start_year"]} to {data["presidents"][i]["term"]["end_year"]}.")
#         print(
#             f"His vice president(s) was/were {data["presidents"][i]["vice_president"]}")

# 1
# for i in range(0, len(data["presidents"])):
#    print(data["presidents"][i]["name"])
