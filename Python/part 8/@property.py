#We use @property decorator on any method in the class to use the method as a property.
#for -->
#EX..1
class Student:
    def __init__(self,math ,chem,phy):
        self.math = math 
        self.phy = phy
        self.chem = chem 


    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"
    
stu1 =  Student(98 , 67, 99)
print(stu1.percentage)

stu1.phy  = 86
print(stu1.percentage)#this is the way you change or renew the value of the of any object value.
 
    