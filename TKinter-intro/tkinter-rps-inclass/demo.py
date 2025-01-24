import my_first_module as mfm
import point


def main():
    # print(f"MAIN")
    print(f"Method from another module: {mfm.add(7, 8)}")
    mypoint = point.Point(5, 4)  # calls a class constructor
    my_other_point = point.Point(7, 8)
    # using a class method
    print(mypoint.calculate_distance(my_other_point))

    # using a class method
    print(point.Point.find_distance_between_points(mypoint, my_other_point))
    mypoint.draw()

    print(mypoint.default_color)
    print(my_other_point.default_color)
    # Change class attribute
    point.Point.default_color = "blue"
    print(mypoint.default_color)
    print(my_other_point.default_color)

    print(mypoint)

    p1 = point.Point(0, 0)
    p2 = point.Point(0, 0)
    print(p1 == p2)


if __name__ == "__main__":
    main()
