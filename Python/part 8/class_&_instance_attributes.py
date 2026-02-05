#These are two types of attributes.
'''
------------->
class.attr--(THESE ARE GENERALLY COMMOM FOR ALL FUNCTION SO WE WRITE THIS IN CLASS )
-----><-------)
obj.attr---(THESE ARE NOT COMMON )
------------->

#NOTE--> say can say that the respect of class attr is greater than object attr.
'''
class Student:
    college_name = "ABC Colllege"
    name = "anonymous" #class attr

    def __init__(self,name,marks):
        self.name = name #object attr
        self.marks = marks 
        print("adding new stundent in database...")

s1 = Student("amit",91)
print(s1.name)        