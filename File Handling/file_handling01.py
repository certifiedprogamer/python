def main():
    # opening a file
    # note: we're going to learn a better way, but we'll start here.
    # r means read, w means write, and a means append.
    garfield_file = open("garfield.txt", "r")
    # garfield_data = garfield_file.read()
    # print(garfield_data)
    # print("g")
    # print("g")

    for line in garfield_file:
        print(line, end="")
    garfield_file.close()


if __name__ == "__main__":
    main()
