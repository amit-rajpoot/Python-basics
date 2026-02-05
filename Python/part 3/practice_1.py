# WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
list = []
movie_1  = input("enter your movie1:")
movie_2  = input("enter your movie2:")
movie_3  = input("enter your movie3:")
movies = movie_1,movie_2,movie_3
(list.append(movies))
print(list)

# WAP to check if a list contains a palindrome fo elements.(hint:usecopy()method).
list1 = [1,2,3,2,1]
 
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

#WAP to count the number of students with the "A" grade in the following tuple.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#store the above values in a list & sort them from "A"to "D"
list3 = ["C","D","A","A","B","B","A"]
list3.sort()
print(list3)



