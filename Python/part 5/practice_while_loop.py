# Print numbers from 1 to 100
x = 1
while x <= 100:
    print(x)
    x += 1
    
# Print numbers from 100 to 1
y = 100
while y >= 1:
    print(y)
    y -= 1   

# Print the multiplication table of a number n.
n = int(input("enter the number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# Print the elements of the following list using a loop.
#[1,4,9,16,25,36,49,64,810]
list = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1

# Search for a number x in this tuple using loop.
#[1,4,9,16,25,36,49,64,81]
nums = [1,4,9,16,25,36,49,64,81]

z = 36

l = 0
while l < len(nums):
 if(nums[l] == z):
    print("found at idx", l)
    break
 else:
    print("finding..")
    l += 1