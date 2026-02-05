#They are function that belong to objects.

#(CREATING CLASS)-->
'''class Student:
       def __init__(self,fullname):
           self.name = fullname  '''

#(CREATING OBJECT)-->
'''s1 = Student("amit")
   s1.hello()    ''' #This is {object.method()}

#(METHOD)-->
'''def hello(self):                   
    print("hello",self.name)  ''' # NOTE-->self parameter must be giving


#EX..1
class Student:
    college_name = "ABC Colllege"
    name = "anonymous" #class attr

    def __init__(self,name,marks):
        self.name = name #object attr
        self.marks = marks 
        
        
    def hello(self):# (method..1)                   
     print("hello",self.name,"your score was-->",self.marks)
    
    def get_marks(self):# (method..2)
       return self.marks
          

s1 = Student("Amit",91)
s1.hello()
print(s1.get_marks())   