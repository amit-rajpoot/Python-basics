# <---(FUNCTIOMS)---> #
'''block of statements that perform a specific task.'''
# SYNTAX--->def func_name(param 1,param 2..):
#            '''some work'''
#               return val
#    func_name(arg1, arg2..)# functoin call  

#EX...1
def sum( a, b ): #parameters
    s = a + b
    return s
print(sum(2,9)) #Function call with print statement; arugument

#We can also write as 
#(i)--->
def sum(a,b):
    return a + b
print(sum(2,9))
#(ii)--->
def calc_sum(a,b):
    return a + b

sum = calc_sum(1,2)
print(sum)

# The function which does not return any value 
def print_hello():
    print("hello")

output  = print_hello()
print(output) 

# WAP to calculate the average of three number.
def cal_avg(a,b,c):
    return (a + b + c)/ 3

average = cal_avg(1,2,3)
print(average)
#OR
def cal_avg(a,b,c):
    sum = a + b + c
    return sum/3

average = cal_avg(1,2,3)
print(average)