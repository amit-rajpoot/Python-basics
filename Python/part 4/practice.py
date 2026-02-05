#Ex..1-->store followong meanings in a python dictionary:
# table : "a piece of furniture","list of facts & figures"
# cat : "a smaal animal"

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}
print(dict)

#You are given a list of subjects for students. Assume one classroom is required for 1
#subject. How many classrooms are needed by all students.
#”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(subjects)

#WAP to enter marks of  3 subjects from the user and store them in a dictionary.start with 
# am empty dictionary & add onr by one . use subject name as key & marks as value.

marks = {}
x = int(input("enter the physics:"))
marks.update({"physics":x})

y = int(input("enter the chemistry:"))
marks.update({"chemistry":y})

z = int(input("enter the math:"))
marks.update({"math":z})

print(marks)


#figure out a way to store 9 & 9.0 as separate values in the set.(you can take help of built-in data type).

values = {9,"9.0"}
print(values)

#<-----OR----->#
values2 = {
    ("float",9.0),
    ("int", 9)
}
print(values2)