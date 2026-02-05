# <---RECURSION--->
# when a function calls itself repeatedly.
#EX..1
def show(n):
    if(n == 0):# Base case--->(agar ye nhi diya toh kuch nhi chalega ye infinte hojaye ga). 
        return
    print(n)
    show(n-1)
    print("END")
show(5) #5, (4 = n-1), (3 = n-2), (2 = n-3), (1 = n-4)

#EX..2
def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n

print(fact(5))