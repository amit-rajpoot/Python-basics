#Create a new file “practice.txt” using python. Add the following data in it:
''' Hi everyone
we are learning File I/O
using Java.
I likAe propgranmming in Java.'''

with open("practice.txt", "w")as f:
    f.write("Hi everyone\nwe are learning File I/O\n")

    f.write("using Java\nI like propgranmming in Java")

#WAF that replace all occurrences of “java” with “python” in above file.
with open("practice.txt", "r")as f:
 data =  f.read()

 new_data = data.replace("Java","python")
 print(new_data)

with open("practice.txt","w") as f:
   f.write(new_data)  

#Search if the word “learning” exists in the file or not.
def check_for_word():
 word = "xlearning"
 with open("practice.txt","r") as f:
   data = f.read()
   if(word in data):
      print("Found")
   else:
      print("not found") 

check_for_word()

#WAF to find in which line of the file does the word “learning”occur first.Print -1 if word not found.
def check_for_line():
   word = "learning"
   data = True
   line_no = 1
   with open("practice.txt","r") as f:
      while data:
        data = f.readline()
        if(word in data):
           print(line_no)
           line_no +=1

   return -1
check_for_line()

# from a file contaning numbers seprated by comma,print the count of even numbers.   with open("practice2.txt","r") 
count = 0
with open("practice2.txt","r") as f: 
   data  = f.read()
   
   nums = data.split(",")
   for val in nums:
       if(int(val) %2  == 0):
          count += 1
print(count)




