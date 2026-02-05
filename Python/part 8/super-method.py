# super() method is used to access methods of the parent class.
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calls Parent constructor
        print("Child constructor")

obj = Child()
#This is part of in