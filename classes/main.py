import my_module as mm
import my_class as student_class


def main():
    # mm.say_something_smart()
    student = student_class.Student()
    student.say_hello()
    student2 = student_class.Student()
    student2.first = "Bob"
    student2.last = "Marley"
    student2.gpa = 3.2
    student2.say_hello()
    student3 = student_class.Student(
        first="John", last="Lennon", gpa=2, scores=[0, 8, 4])
    student3.say_hello()
    print(student3)


if __name__ == "__main__":
    print(__name__)
    main()
