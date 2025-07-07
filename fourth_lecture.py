# dictionary

# info = {
#     "name" : "Dipesh",
#     "subjects" : ["Python", "Java", "C++"],
#     "marks" : {
#         "Python" : 90,
#         "Java" : 95,
#         "C++" : 98
#     },
#     "percentage" : 88.33,
#     "age" : 20,
#     "city" : "Mumbai"
    

# }

# print(info["name"])
# print(info["subjects"])
# print(info["marks"]["Python"])
# print(info["percentage"])
# print(info["age"])
# print(info["city"])

# info["name"] = "0 7"
# print(info["name"])



# null dictionary


# info = {}
# info["Name"]= "Dipesh"
# info["Age"]= 20

# print(info)







#nested dictionary


# info = {    "name" : "Dipesh",
#             "subjects" : ["Python", "Java", "C++"],
#             "marks" : {
#                 "Python" : 90,
#                 "Java" : 95,
#                 "C++" : 98
#             },
#             "percentage" : 88.33,
#             "age" : 20,
#             "city" : "Mumbai"
# }
# print(info["marks"]["Python"])
# print(info["marks"]["Java"])
# print(info["marks"]["C++"])
# print(info["name"])
# print(info["age"])





# info = { 
#     "name": "Dipesh kewat",
#     "subjects": ["Python", "Java", "C++"],
#     "marks": {
#         "Python": 90,
#         "Java": 95,
#         "C++": 98
#     },
#     "percentage": 88.33,
#     "age": 20,
#     "city": "Mumbai"
# }
# # print(info["name"])
# # print(info["age"])
# # print(info["city"])
# # print(info["subjects"])
# # print(info["marks"]["Python"])
# # print(info["marks"]["Java"])
# # print(info["marks"]["C++"])


# info.update({"name": "Ritik Kewat", "age": 21, "city": "Delhi"})

# print(info["name"])
# print(info["age"])  
# print(info["city"])


 
#PRACTICE QUESTION

# 1st question

# words={
#     "table": ["a piece of furniture", "list of facts and figures"],
#     "cat": "a small Animal"
# }
# print(words)



# 2nd question

# student={"python","python","python", "java","java","java", "c++","c++","javascript","c"}
# print("the number of classes needed:", len(student))




3# 3rd question

# subjects_marks={}
# a=int(input("Physics: "))
# a=int(input("Chemistry: "))
# a=int(input("Maths: "))
# a=int(input("English: "))

# subjects_marks.update({"Physics": a, "Chemistry": a, "Maths": a, "English": a})

# print("marks : ", subjects_marks)





# 4th question

value={"9","9.0"}
print("the type of value is:",value)

value={
    ("float",9.0),
    ("int",9)
}
print("the type of value is:",value)

