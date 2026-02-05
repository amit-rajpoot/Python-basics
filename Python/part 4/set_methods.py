# <---Set methods--->
# set.add(element)--->adds on element.
# set.remove(element)--->removes the element.
# set.clear()--->empties the set.
# set.pop()--->removes a random value.

#[EX..1]-->
collection = set()
collection.add(1)
collection.add("amit")
collection.add((1,2,3,4))
collection.add(4)
collection.remove(1)
print(collection)
print(len(collection))

collection.pop()
print(collection)

collection.clear()
print(collection)

# SOME MORE METHODS--->
# set.union(set2) #combines both set values & returns new.
# set.intersection(set2) #combines common values & returns new.
# EX--->
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))# {1, 2, 3, 4}
print(set1.intersection(set2))



