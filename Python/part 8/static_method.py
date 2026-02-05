#(STATIC METHOD)
#-->Methods that don't use the self parameter (work at class level)
#IF THESE ARE USE SELF PARAMETER SO WE CALLED THAT NON-STATIC METHOD. 
class Student:
   @staticmethod
   def college():
      print("ABC College")

'''#NOTE--> Decorators allow us to wrap another function in order to 
           extend the behaviour of the wrapped function,
           without permanently modifying it.  '''



class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
print(MathOperations.add(5, 3)) 