#(INHERITANCE)--->
'''--> Inheritance allows a class (child/derived class),
       to reuse the properties and methods of another class (parent/base class).
    --> This helps in code reusability and extending functionality.'''


#Single inheritance-->
#EX..1
class Parent:
    def display(self):
        print("This is the Parent class")

class Child(Parent):
    def show(self):
        print("This is the Child class")

obj = Child()
obj.display()  # inherited from Parent
obj.show()   # defined in Child

#EX..2
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def start():
        print("car stop..")


class Totyotacar(Car):
    def __init__(self,name):
        self.name = name

car1 = Totyotacar("fortuner")
car2 = Totyotacar("prius")

print(car1.start())
        
# Multilevel Inheritance-->
#EX..1
class Grandparent:
    def grand(self):
        print("Grandparent")

class Parent(Grandparent):
    def parent(self):
        print("Parent")

class Child(Parent):
    def child(self):
        print("Child")

obj = Child()
obj.grand()
obj.parent()
obj.child()

# Multiple Inheritance ---> 
#EX..1
class Father:
    def skills(self):
        print("Father: Cooking")

class Mother:
    def skills(self):
        print("Mother: Singing")

class Child(Father, Mother):
    def skills(self):
        print("Child: Dancing")

obj = Child()
obj.skills()


