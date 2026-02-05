#Conceptual Implementations in python-->
'''Private attributes & methods are meant to be used only within the class and are not
   accessible from outside he class. '''

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc__pass =  acc_pass 

    def reset_pass(self):
        print(self.__acc__pass)


acc1  = Account("12345" , "abcde")


print(acc1.acc_no) # is wale part mai error nhi ayega
print(acc1.acc__pass()) # is wale part mai error ayega
# Class ke andar wala print hoga par bhar wale print nhi hoga that is called privacy 

class Person:
    __name = "anonymous" '''This can also done by using (__) same as pervious,
                           # only class mai joh fuction hai woh hi akela access karpayega'''

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())# yhe access nhi kar sakta









