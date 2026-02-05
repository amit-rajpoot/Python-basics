# A built-in data type that let us create "immutable" sequences of values
# Tuples are closed in ()prnatesis
# tup[0] = 5 not allowed (assigment) to assign new value
# we can also create the empty tuple--->'''tup =()'''

#EX..1
tup = (1,)# For single data tuple we always use comma 
print(tup)
print(type(tup))

tup = (1)# Otherwise it return  
print(tup)
print(type(tup))

#NOTE-->But for multiple values it is not mandatory 

#EX..2
tup2 = (1,2,3,4)
print(tup2)
print(type(tup2))

#NOTE-->(tuple slicing is just same as we do in list)