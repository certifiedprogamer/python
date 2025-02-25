class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} is working as a {self.position}")


class Manager(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)

    def hold_meeting(self):
        print(f"{self.name} is holding a meeting")


team = [Employee("Alice", "Developer"), Manager(
    "Bob", "Team Lead"), Employee("John", "Unpaid Intern")]

for employee in team:
    employee.work()
    if isinstance(employee, Manager):
        employee.hold_meeting()
