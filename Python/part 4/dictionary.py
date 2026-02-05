# Dictonaries are used to store data values in (key:value) pairs 
# They are unordered,mutable(changeable)& don't allow duplicate keys
# We store int,string,list,boolen,float in dict.
# They are closed in {} curly bracket and sperated by comma
# "synatx"--->(key:value)
# FOR EX..
dict = {
    "name" : "amit",
      "age" : 17.5 ,
    "marks" : [67,55,43]
}
#print(dict)

#EX..1
info = {
    "name" : "amit",
      "age" : 17.5 ,
    "marks" : [67,55,43],
    "blood group" : "A+" ,
    "is_adult" : True   
}
print(info)
print(type(info))
#For access any data in dict we simpliy use search by its key b value
print(info["name"])
#For assign new value 
info["age"] = 17
print(info)

#EX..2
null_dict = {}
null_dict["name"] = "apancollege"
print(null_dict)

