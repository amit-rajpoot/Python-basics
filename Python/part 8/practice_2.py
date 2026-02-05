#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,balance,acc):
        self.balance = balance
        self.account_no = acc


    def debit(self, amount):
     self.balance -= amount
     print("Rs",amount,"was debited")
     print("total balance = ", self.get_balance())


    def credit(self,amount):
     self.balance += amount
     print("Rs",amount,"was credit")
     print("total balance = ", self.get_balance())


    def get_balance(self):
     return self.balance

#Object
a1 = Account(20000,12344)
a1.debit(1000)
a1.credit(3000)

#Printing balance
#print(a1.balance)
        
    