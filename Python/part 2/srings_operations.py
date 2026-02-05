# STRINGS
''' 
-->Concatenation 
   "hello" + "world" -----> "helloworld"
   
--> Length of str
    len(str)--> from this we can find the string length'''

str1 = "hello"
str2 ="world"
Final_str = str1 + str2
print(Final_str)
print(len(Final_str))
# NOTE--> spaces also calculate in len()

# STRING FUNCTIONS
str = "i am coder."
print(str.capitalize()) #capitilizes 1st character
print(str.endswith("er.")) #returns true value if string ends with substring
print(str.replace("coder", "ohyes")) # it will replace the character
print(str.find("o")) #returns 1st index if 1st occurrence
print(str.count("am")) #counts the occurrence of substring in string
