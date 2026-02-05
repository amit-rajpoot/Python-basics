# <---FOR_LOOPS--->
'''loops are used for sequential traversal.for traversing list, string, tuples etc.'''
#for loops
'''for element in list:
   # some work
'''
# EX...1
list = [1, 2, 3]
for val in list:
    print(val)

# EX...2
tup = (1,2,34,4,5,6,78,8,9)
for val in tup:
    print(val)


#for loop with else--->{these are only use for work end of the loop}
'''for el in list
       # some work
   else:
    #work when loop ends'''
# EX...1
str = "amit rajpoot"
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)  
else:
     print("END")
    