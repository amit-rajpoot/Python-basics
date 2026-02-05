#Define a Circle class to create a circle with radius r using the constructor.

#Define an Area) method of the class which calculates the area of the circle.

#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return(22/7) * self.radius
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

#Define a Employee class with attributes role, department & salary. This

#showDetails() method.

#Create an Engineer class that inherits properties from Employee &

#attributes: name & age.


class Employee:
    def __init__(self,role,dept,salary):
      self.role = role 
      self.dept = dept 
      self.salary = salary

    def showDetails(self):
          print("role = ", self.role)
          print("dept = ", self.dept)
          print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        super().__init__("engineer","ET", "75000")

engg1 = Engineer("Elon musk", 40)
engg1.showDetails()
#e1 = Employee("accontant","finance","60000")
#e1.showDetails()


#Create a class called Order which stores item & its price.

#Use Dunder functiongt() to convey that: order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
      return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea",15)

print(odr1> odr2)
