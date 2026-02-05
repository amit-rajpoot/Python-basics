# <---Break--->
'''used to terminate the loop when encountered.'''
#<---continue--->
'''Terminates execution in the current ilteration & continues execution of the loop with 
the next ilteration'''

# EX...1
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("End of loop")

# EX...2
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# EX...3
i = 0
while i <= 100:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1