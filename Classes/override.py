class Parent:
    def overide(self):
        print("Parent")

class Child(Parent):
    def overide(self):
        print("child1")
        super().overide()
        print("child2")


child = Child()
parent = Parent()

child.overide()
parent.overide()