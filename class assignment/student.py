class Student:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def pass_or_fail(self):
        if self.grade > 60:
            print("Pass")
        else:
            print("Fail")


student = Student("John", 75)
student.pass_or_fail()
