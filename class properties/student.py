class Student:
    def __init__(self, name="juf", grade=2):
        self.name = name
        self.grade = grade
        self._status = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 1:
            raise ValueError("Name length must be at least 2 characters")
        self.__name = name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")
        self._grade = value

    @property
    def status(self):
        if self.grade >= 60:
            return "Pass"
        else:
            return "Fail"


s = Student()
s.name = "Alice"
s.grade = 85
print(s.status)
s.grade = 45
print(s.status)
