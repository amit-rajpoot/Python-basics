# MOST USED METHODS
# myDict.keys( ) # returns all keys
# myDict.items( ) # returns all (key, val) pairs as tuples
# myDict.update( newDict ) # inserts the specified items to the dictionary
# myDict.values( ) # returns all values
# myDict.get( “key"  ) # returns the key according to value

info = {
    "name" : "amit",
      "age" : 17.5 ,
    "marks" : [67,55,43], 
    "sub" :{
        "chem" : 93,
        "phy" : 98
    }  
}
print(info.keys())#nested keys are not added in this function
print(info.values())
print(info.items()) # For single in single pair we can easily use as print(pairs[1])
print(info.get("name"))
'''why we use this method instead of dict["key"]
because if we put wrong value in it this does not
error instead of this it will none. 
# For ex-->
 stundent = { "name" : "amit",
      "age" : 17.5 ,
    "marks" : [67,55,43], 
    "sub" :{
        "chem" : 93,
        "phy" : 98 }
# ye ham ko help karta hai baki ke code ko run karne mai madath karta hai
print(stundent["name2"])# output--> error
print(stundent.get("name2))# output--> none'''

new_info = {"city":"jhansi"}
info.update(new_info)
print(info)


#for converting into list with help of type casting
print(list(info.keys()))
print(list(info.values()))
#for length
print(len(list(info.keys())))
print(len(list(info.values())))


