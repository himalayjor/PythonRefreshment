class Person(object):
    pass

class Employee(Person):
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

class AmazEmployee(Employee):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id


amazEmployee = AmazEmployee("HMJ", "1")

amazEmployee.printName()

print(amazEmployee.id)