#function
# Function to calculate the sum of two numbers
# and print the result

def calcSum(a,b):
    sum=a+b
    print(sum)
calcSum(5,8)
calcSum(7,12)
calcSum(9,4098)
calcSum(7856785,8)






# Function to calculate the sum of two numbers
# and return the result

def calcSum2(a,b):
    sum=a+b
    return sum
calcSum2(5,8)
result = calcSum2(7,12) 
print(result)






#calculate the average of 3 umbers


def calcavg(a,b,c):
    avg = (a + b + c) / 3
    print(avg)

calcavg(5,8,9)
calcavg(7,12,15)
calcavg(9,4098,1000)
calcavg(7856785,8,1000000)


#Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.


# Function to print the name of two children
def child(child1 , child2):
    print("The Oldest son is "+child1)
    print("The Youngest son is "+child2)
child(child1="Light", child2="Ritik")









# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:


def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")












# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
#CODE

def hero(**heros):
    print("the real heros is "+heros["name1"])
    print("the fake hero is  "+heros["name"])

hero(name="Ritik", name1="Dipesh")





# Default Parameter Value
# If you do not provide a value for the parameter, the default value will be used.
#code


def country( name="India",):
 print("I m from " + name)
country("Australia")
country("USA")
country("Italy")
country()  # This will use the default value "India"
country("Japan")
country("Germany")
country("korea")  # This will again use the default value "India"






# Passing a List as an Argument
# You can send any data types of arguments to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#code



#Quetion 1 - WAP to conver USD to INR

def converter(usd):
    inrvalue=usd*86
    print(usd,"USD =", inrvalue,"INR")

converter(1)
converter(10)
converter(173)




# Question 2 - WAP to find the area of a rectangle
def area(length, breadth):
    area = length * breadth
    print("Area of rectangle is", area)

area(5, 10)
area(7, 12)
area(9, 15)
area(7856785, 8)


#question 3 - WAP to find the number enter by the user is even or odd

def evenodd(num):
    num=int(input("Enter a number: "))
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

evenodd(num=0)
















#Recursion
# A function that calls itself is called a recursive function.
# A recursive function must have a base case to stop the recursion.

def show(n):
        if n==0:
            return
        print(n)
        show(n-1)
show(5)



def show(n):
        if n==0:
            return
        print(n)
        show(n-1)
        print("Recursion")
show(5)





# Factorial using recursion

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Output: 120
print(factorial(6))  # Output: 720
print(factorial(17))  # Output: 355687428096000
print(factorial(8))  # Output: 40320
print(factorial(9))  # Output: 362880
print(factorial(10)) # Output: 3628800
print(factorial(11)) # Output: 39916800


#question 1 - WAP to find the sum of first n natural numbers using recursion

def nsum(n):
    if n == 0:
        return 0
    else:
        return n + nsum(n - 1)

print(nsum(5))  # Output: 15 (5 + 4 + 3 + 2 + 1 + 0)
print(nsum(10))  # Output: 55 (10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0)
print(nsum(20))  # Output: 210 (20 + 19 + 18 + 17 + 16 + 15 + 14 + 13 + 12 + 11 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0)
print(nsum(100))  # Output: 5050 (100 + 99 + 98 + ... + 1 + 0)
print(nsum(50))  # Output: 1275 (50 + 49 + 48 + 47 + 46 + 45 + 44 + 43 + 42 + 41 + 40 + 39 + 38 + 37 + 36 + 35 + 34 + 33 + 32 + 31 + 30 + 29 + 28 + 27 + 26 + 25 + 24 + 23 + 22 + 21 + 20 + 19 + 18 + 17 + 16 + 15 + 14 + 13 + 12 + 11 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0)


#question 2 - WAP using recursive function to print all elements in a list
#hint: use list and Index as parameters

def print_list(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_list(lst, index + 1)

animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Bear"]
print_list(animals)





def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Bear"]
print_list(animals)

