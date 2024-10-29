
def main():
    while True:
        resp = input("Tell me something about Odie: ")
        if resp == "q":
            break
        else:
            file = open("odie.txt", "a")
            file.write(resp + "\n")
            file.close()


def write_list_to_file():
    about_odie = ["he's yella\n",
                  "he's garfield's friend\n" "his girlfirend is a brush\n"]

    file = open("odie.txt", "w")  # overwriting existing file
    file.writelines(about_odie)
    file.close()


def write_with_with():
    about_odie = ["he's yella\n",
                  "he's garfield's friend\n" "his girlfirend is a brush\n", "written with with\n"]

    with open("odie.txt", "w") as file:
        file.writelines(about_odie)


if __name__ == "__main__":
    # main()
    # write_list_to_file()
    write_with_with()
