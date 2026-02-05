#THEROY
list = [2, 1, 3]
#list.append(4) -->adds one element at the end[2,1,3,4] 
#list.sort( ) -->sorts in ascending order[1, 2, 3]
#list.sort(revers=true) -->sorts in desending order[3,2,1]
#list.reverse( ) -->reverses list[3,1,2]
#list.insert( idx, el ) -->insert element at index

#EX..1
list_1 = [2,3,4,4,3]
(list_1.append(9))
print(list_1)
(list_1.sort())
print(list_1)
(list_1.sort(reverse=True))
print(list_1)
(list_1.reverse())
print(list_1)
(list_1.insert(4,3))
print(list_1)
print("example..1 done")

#FOR removing and pop out the elements we use 
list = [2,1,3,1]
#list.remove(element)-->removes first occurrence of element[2,3,1]
#list.pop(index)-->removes element at index

#EX..2
list_2 = [2,1,3,1]
#list_2.pop(2)
print(list_2)
list_2.remove(1)
print(list_2)
print("exmaple..2 done")