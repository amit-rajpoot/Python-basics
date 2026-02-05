#WAF to print the length of a list. ( list is the parameter)
num = [1,3,4,5,3,5,3,5,3,5,3,5,6]
num2 = [2,4,5,5,6,7,8,6,4,3,12,3,6]

#function
def print_len(list):
 print(len(list))

#function call
print_len(num)
print_len(num2)

#WAF to print the elements of a list in a single line. ( list is the parameter)
list3 = [3,3,4,5,6,4]
def print_list(list):
 for item in list:
  print(item, end=" ")

print_list(list3)

#WAF to find the factorial of n. (n is the parameter)
def cal_fact(n):
    fact= 1
    for i in range(1,n+1):
        fact  *=  i
    print(fact)

cal_fact(6)

#WAF to convert USD to INR.
def converter(usd_val):
  inr_val = usd_val * 83
  print(usd_val,"usd = ",inr_val,"INR")

converter(10)

#compl
def in_val(n):
 if (n%2 == 0):
  print("function is EVEN")
 else:
  print("function is ODD")

in_val(2)