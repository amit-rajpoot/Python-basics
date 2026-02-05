# IF-ELIF-ELSE

'''SYNTAX---->'''
'''if(condition):
        statement 1
   elif(condition):
        statement 2
   else:
        staement __  '''


#EXE--->1
age = int(input("enter your age:"))

if(age >= 18):
    print("can vote and apply for license")
else:
     print("can not vote and apply for license ")
#EXE--->2
light = input("enter the color:")
if(light == "green" ):
    print("go")
elif(light == "yellow"):
    print("wait")
elif(light == "red"):
      print("stop")
else:
     print("ruko matt chale jao")  
         
print("END OF CODE")         
   
#EXE--->3
Marks =int(input("enter the student marks:"))
if(Marks >= 90):
     print("grade A")
elif(Marks >= 80 and Marks > 90):
     print("grade B")
elif(Marks >= 70 and Marks > 80):
     print("grade C")
elif(Marks > 70):
     print("grade D")
else:
     print("fail")


# NESTING
Age= 34 
if(Age >= 18):
     if(Age >= 70):
          print("cannot drive")
     else:
          print("can drive")

else:
  print("cannot drive")