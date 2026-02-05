# WAP to print the elements of the following list using a loop.\
list = [1,4,9,16,25,36,49,64,81,100]
for val in list :
    print(val)

# WAP to search for a number x in this tuple using loop.
num = int(input("enter the number"))
tup = (1,4,9,16,25,36,49,64,81,100)
for val in tup :
    if (val == num):
     print("enter number  is found")
     break
    print(val)
else: 
      print("END")
# NOTE--->This method is called liner search. 