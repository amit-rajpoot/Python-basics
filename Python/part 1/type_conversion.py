# Type conversion
# a = "3" we can not add to allow sting + float 
a = 10
b = 12.5
sum = (a + b)
print(sum)
print(type(sum))

# Tpye casting
a = float("3")
b = 4.25
print(type(a))
print(a + b)
 
#Theory 
'''Typecasting (Explicit Conversion): The programmer manually converts a data type to another using functions like int(), float(), etc., which may lead to data loss.
Type Conversion (Implicit Conversion): Python automatically converts compatible data types during operations without user intervention, ensuring no data loss.'''