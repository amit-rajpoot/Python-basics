#Similar to the string slicing.
#SYNTAX------>
'''list_name[start_idx:ending_idx]'''
#NOTE-->ending index is not include.
#      0  1  2  3  4  5  6  -->positive indexing
marks=[54,45,43,54,43,45,56]
#      -7 -6 -5 -4 -3 -2 -1 -->negative indexing  
print(marks[1:])
print(marks[2:5])
print(marks[0:])
print(marks[-5:-3])
print(marks[-7:])
print(marks[:-1])
print(marks[:])
