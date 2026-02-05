'''with open("demo.txt" , "a")as f:
            data = f.read()'''
#it is also the way write the file.
with open("demo5.txt" , "a") as f:
   data =  f.read()
   print(data)

#NOTE -->close syntax is not neccesary for with syntax because it automatic close the file.

with open("demo5.txt" , "w") as f:
   f.write("new data")

