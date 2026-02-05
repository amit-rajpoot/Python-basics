# <<---RANGE--->>
'''range functions returns a sequence of number , 
starting from 0 by default, and increments by 
"1" (by default), and stops before a specified number. '''
# NOTE-->"ENDING NUMBER IS NOT INCLUDED"
#SYNTAX---> range(start?,stop,step?)
for el in range(5):#range(stop)
    print(el)
for el in range(2,10):#range(start,stop)
    print(el)
for el in range(2,10,2):#range(start,stop,step)
    print(el)

#EX...1
print(range(5))

#EX...2
seq = (range(5))
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

#EX...3-->by using for loop
seq = (range(5))

for i in seq:
    print(i)