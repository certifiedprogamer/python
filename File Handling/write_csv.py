import csv

data = [
    ["character", "age", "favorite subject"],
    ["Ms. Frizzle", 30, "bus driving"],
    ["Arnold", 12, "science"],
    ["Maggie", 11, "math"]
]

with open("msb.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
