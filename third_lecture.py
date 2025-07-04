# List

# # marks=[23,45,67,89,90,34,5,6,78,98]
# # print("Marks :", marks[0])
# # print("Marks :", marks[1])
# # print("Marks :", marks[2])
# # print("Marks :", marks[3])
# # print("Marks :", marks[4])
# # print("Marks :", marks[5])
# # print("Marks :", marks[6])
# # print("Marks :", marks[7])
# # print("Marks :", marks[8])
# # print("Marks :", marks[9])
# # print("Marks :", marks[0:4])
# # print(len(marks))


# marks = [23, 45, 67, 89, 90, 34, 5, 6, 78, 98]
# print("Marks :", marks[-7:-1])  # Slicing from index -7 to -2
# marks[0] = 100
# print("Marks :", marks)


# list=[1, 2, 3, 4, 5, 6, 7, 8, 9,]
# list.append(7)
# print("List :", list)

# list = [11, 12, 13, 4, 5, 6, 17, 8, 19,4,6,1, 2, 3, 4, 5, 6, 7, 8, 9]
# list.sort()
# print("List :", list)


# list = [11, 12, 13, 4, 5, 6, 17, 8, 19, 4, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list.sort(reverse=True)  # Sorting in descending order
# print("List :", list)

# fruits= ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# fruits.sort(reverse=True)  # Sorting in ascending order
# print("Fruits :", fruits)


# list=[12, 34, 56, 78, 90, 23, 45, 67, 89, 100]
# list.reverse()  # Reversing the list
# print("List :", list)


# list = [12, 34, 56, 78, 90, 23, 45, 67, 89, 100]
# list.insert(5,99999)
# print("List: ",list)

# list = [12, 34, 56, 78, 90, 23, 45, 67, 89, 100]
# list.remove(12)
# print("List: ",list)


# list = [12, 34, 56, 78, 90, 23, 45, 67, 89, 100]
# list.pop(5)  # Removing the element at index 5
# print("List: ",list)



#Tupples

# tup=(1,3,5,7,3,2,6,78,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,99)
# print(tup)
# print(tup[0])  # Accessing the first element
# print(tup[1])  # Accessing the second element
# print(tup.index(3)) # Finding the index of the first occurrence of 3
# print(tup.count(9))  # Counting the occurrences of 9





# 1st question

# movies=[]
# movie1=input("Enter the name of the first movie: ")
# movie2=input("Enter the name of the second movie: ")
# movie3=input("Enter the name of the third movie: ") 
# movie4=input("Enter the name of the fourth movie: ")
# movie5=input("Enter the name of the fifth movie: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# movies.append(movie4)
# movies.append(movie5)    

# print("Movies List:", movies)


# 2nd method

# movies=[]
# movies.append(input("Enter the First Movie Name: "))
# movies.append(input("Enter the Second Movie Name: "))
# movies.append(input("Enter the Third Movie Name: "))
# movies.append(input("Enter the Fourth Movie Name: "))
# movies.append(input("Enter the Fifth Movie Name: "))

# print("Movies List:", movies)




# 2nd question

# list1=[1,2,3,2,1]

# copy=list1.copy()  # Copying list1 to copy
# copy.reverse()

# if copy==list1:
#     print("List1 is a palindrome")
# else:
#     print("List1 is not a palindrome")


# list2=[1,2,3,2,1,1]

# copy=list2.copy()  # Copying list2 to copy
# copy.reverse()

# if copy==list2:
#     print("List2 is a palindrome")
# else:
#     print("List2 is not a palindrome")



# 3rd question

grade=["A","B","C","D","A","A","B","C","E","D","A","B","B","D","D","D","D","A","A","A","A","B","B","B","B","E","F"]

print("Grade List:", grade.count("A"))
print("Grade List:", grade.count("B"))
print("Grade List:", grade.count("C"))
print("Grade List:", grade.count("D"))
print("Grade List:", grade.count("E"))
print("Grade List:", grade.count("F"))

grade.sort()
print("Grade List:", grade)  # This will raise an error because tuples are immutable
# Tuples cannot be sorted in place, but you can convert it to a list, sort
