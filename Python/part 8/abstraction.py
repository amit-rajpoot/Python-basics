#THERE ARE FOUR PILLAR OF OOPS--->
'''
(i)->Abstraction
(ii)->Encapsulation
(iii)->Inheritance
(iv)->Polymorphism

'''
#ABSTRACTION->
'Hiding the implementation details of a class and '
'only showing the essential features to the user.'

#EX..1
class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.cluch = False
    def start(self):
        self.cluch = True
        self.acc = True
        print("car get start...")

car1 = Car()
car1.start()


 
#ENCAPSULATION->
'Wrapping data and functions into a single unit (object).'
