#<----WRITING TO FILE---->
#<<--SYNTAX-->>
''' f = open("demo.txt","w")
    f.write("this is a new line") #overwrites the entire file'''

#EX..1
f = open("demo.txt" , "a")
f.write("\ni want learn java.123")#Tjis was added to old data
f.close

# This will also create this file withount any existance.
#EX..2
f = open("sample.txt" , "w")
f.close()

f = open("sample2.txt" , "a")
f.close()

# "r+"mode used to add the data at starting.
f = open("demo2.txt","r+")
f.write("abc")
f.close()

# "w+"mode erase the old data nad then you can add anything.
f = open("demo3.txt","w+")
f.write("abc")
f.close()
# "a+"
f = open("demo4.txt","a+")
#f.write("abc")
print(f.read())
f.write("abc")
f.close()
# NOTE-->
'''r+ --->no truncate(pointer at the start)
   w+---> truncate
   a+--->no truncate(pointer at the end)'''