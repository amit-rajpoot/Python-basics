# SLICING
'''Slicing in Python is a technique used to extract specific portions of sequences like lists, strings, or tuples. 
It allows you to access a range of elements by specifying a start, stop, and step value.'''
#Syntax
'''sequence[start:stop:step]'''
'''
start: The index where the slice begins (inclusive). Defaults to 0 if omitted.
stop: The index where the slice ends (exclusive).
step: The interval between elements. Defaults to 1 if omitted.'''

# NOTE -->ending index was not included

str1 = "My name is amit rajpoot"
print(str1[0:4])
print(str1[-3:-1])
