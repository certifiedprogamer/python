import my_first_module as mfm
import point


def main():
    # print(f"MAIN")
    print(f"Method from another module: {mfm.add(7, 8)}")
    mypoint = point.Point()  # calls a class constructor
    mypoint.draw()


if __name__ == "__main__":
    main()
