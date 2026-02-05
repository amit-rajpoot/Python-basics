# WAP to find the sum of first n numbers.(using while)
n = int(input("enter the number : "))
sum = 0
count = 1
while count <= n:
  sum += count
  count += 1   
    
print("The sum of the number : ",sum)

# WAP to find the find the factorial of first n numbers.(using for)
n = int(input("enter the number : "))
fact = 1
for i in range(1,n+1):
  fact *= i

print("The fact of n number : ",fact)
