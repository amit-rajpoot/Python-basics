#POLYMORPHSIM:(OPERATOR OVERLOADING)
#--> When the same operator is allowed to have different meaning according to the context.

# What is operator overloading ?
# with example--> we fint it  (code.)
'''
   print(1 + 2) # 3
   print ("AMIT" + "RAJPOOT) # concatenate
   print[1,2,3] + [4,5,6] # merge 

''' #as we can see that the "+" doing many different work(This is operator overloading).

#(OPERATORS &DUNDER FUNCTIONS)-->
'''
a+b    #addition          a._add__(b)

a-b    #subtraction       a.__sub_(b)

a*b    #multiplication    a_mul____(b)

a/b    #division          a._truediv.(b)

a%b    #addition          a._mod__(b)

'''# There are many more.


#EX..1(To print complex number.)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", + self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


# Testing
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2   # uses add
num3.showNumber()

num4 = num1 - num2   # uses sub
num4.showNumber()
        
