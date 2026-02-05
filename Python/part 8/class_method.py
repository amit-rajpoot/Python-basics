# A class method is bound to the class & recevies the class as an implict first argument.

#NOTE--> static method can't access or modify class state & generally for utility.


class Stundent: 
    @classmethod # DECORATOR
    def college(cls):
        pass

#"cls" use an arrgument.

#Ex..1
class Person:
    name = "anonymous"


    @classmethod
    def changeName(clas,name):
        clas.name = name

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

#INSHORT-->Yhe direct change karta hai value from class. 