#Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:
   def __init__(self,name,marks):
      self.fullname = name
      self.marks = marks
      
    
    # METHOD--> 
   def get_avg(self):
       sum = 0
       for val in self.marks:
           sum += val
       print("Hello",self.fullname,"your marks average is-->",sum/3)

s1 = Student("Amit", [99,88,89])     
s1.get_avg()

