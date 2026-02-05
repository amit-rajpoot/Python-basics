#(__init__function)-->
#{CONSTRUCTOR}-->
'''
All classes have a function called_init_(),
 which is always executed when the class is being initiated.

# creating class-->               |   # creating object  
class Stundent:                   |   s1 =  Stundent()
  def __init__(self,fullname):    |   print(s1.name)
     self.name = fullname         | 

    
#NOTE-->"The self parameter is a reference to the current instance of the class,
          and is used to access variables that belongs to the class."
'''
#EX..1
class Student:
    def __init__(self,name,grade): #FUNCTION..1
     self.name = name
     self.grade = grade
    
#OBJECT
student1 = Student('amit',11)
print(student1.name , student1.grade)

student2 = Student('riya',12)
print(student2.name,student2.grade)


#There are two types of constructor--->

#(i)-->(DEFAULT CONSTRUCTORS)
def __init__(self):
   pass

#(ii)-->(PARAMETRIZED CONSTRUCTORS)
def __init__(self,name,marks):
   self.name = name
   self.marks = marks
   print("adding new student in data base.")