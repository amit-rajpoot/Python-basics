# You can delete attributes (instance variables) of an object using---> 
''' del '''
#EX...1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Amit", 22)

print(s1.name)  # Amit

del s1.name     # deleting the attribute
# print(s1.name)  # ❌ AttributeError
 
# Agar print karoge toh-->
#print(s1.name)