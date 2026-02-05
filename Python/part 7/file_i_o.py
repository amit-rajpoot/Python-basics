# <---FILE I/O--->
# "I" means input and "O" means output.
# python can be used to perform operaters on  a file . (read & write data)
# types of all files--->
'''(i)->TEXT_FILES->txt ; docx ; log .
   (ii)->BINARY_FILES->mp4 ; mov ; pug ; jpeg.'''

# Open , read & close file.
'''We have to open a file before reading or writing.'''
# SYNTAX-->
# f = open("file_name","mode")
''' (file_name)-->like-->(sample.txt , demo.docx)
    (mode)-->like-->(r:read mode , w:write mode)  '''
# NOTE--->agar hamne mode justify nhi kiya hai toh python usse by default (read mode) mai considerd karega.

#EX..1

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()#This is important for closing the nhi toh file chori hojaye gi.

# Different modes of for data;
# (CHARACTER)                (MEANING)
#     'r'----> open for reading(default).
#     'w'---->open for writing,truncating the file first.
#     'x'---->create a new file and open it for writing.
#     'a'---->open for writing,appending to the end to the end of the file if it exists.
#     'b'---->binary mode.
#     't'---->text mode (default).
#     '+'---->open a disk file for updating (reading and writing).

#For print the file for minimun charcter.(as you want)
f = open("demo.txt","r")
data = f.read(5)# for specfic charater you want to learn.
print(data)
f.close()

#For print the file line by line we used.
'''data = f.readline()'''
f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()


#NOTE--->agar ham ne ek bar pura data read kar liye toh ange kuch print hone bichega nhi toh sirf space print hoga.
f = open("demo.txt","r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)# for print the empty line(because data katam.) 
 
f.close()
