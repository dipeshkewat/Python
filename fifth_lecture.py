#loop

i=10000
while i>=0:
    print(i)
    i=i-1

print("Loop finished")


#  1st Question
#print numbers from 1 to 1000

i=1
while i<=1000:
    print(i)
    i=i+1


# 2nd Question
#print numbers from 1000 to 1

i=1000
while i>=1:
    print(i)
    i=i-1


# 3rd Question
# multiplication table of n number

n=5
i=1
while i<=10:
    print(n*i)
    i=i+1


# 4th Question
# multiplication table of  number given by user
n=int(input("Enter a number for multiplication table: "))
i=1
while i<=10:
    print(n*i)
    i=i+1



# 5th Question
#print the elements of a list using while loop

nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i=i+1


# 6th Question
# search an element in this tuple using while loop


nums=(1,4,9,16,25,36,49,64,81,100)
i=0

search=9
while i<len(nums):
    if (nums[i]==search):
        print("Number found at index", i)
    else:
        print("Number not found")
    i=i+1


# #6th Question
# # search an element entered by the user in this tuple using while loop

nums=(1,4,9,16,25,36,49,64,81,100)
i=0

search=int(input("Enter a number to search in the tuple: "))
while i<len(nums):
    if (nums[i]==search):
        print("Number found at index", i)
    else:
        print("Number not found")
    i=i+1



#break and continue 
#break

nums=(1,4,9,16,25,36,49,64,81,100)
i=0

search=int(input("Enter a number to search in the tuple: "))
while i<len(nums):
    if (nums[i]==search):
        print("Number found at index", i)
        break
    i=i+1
else:
    print("Number not found")



#continue 

i=1
while i<=100:
    if(i%2!=0):
     i+=1
     continue
    print(i)
    i+=1
  

#for Loop

#1st question

nums=[1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

#2nd question

nums=(1,4,9,16,25,36,49,64,81,100,81)
x=81
index=0
for i in nums:
    if(i==x):
        print("the number found at index: ",index)
    index=index+1


#range

i = range(100)
for d in i:
    print(d)




i = range(100)
for d in range(100):
    print(d)




for i in range(2,100,):   #first no is starting range
                          #second no is Ending range 
                          #Third no is step size
        print(i)


for i in range(2,100,2):
        print(i)

for i in range(1,100,2):
        print(i)





#1st question
#print 1 to 100 numbers

for i in range(100):
 print(i)



#2nd question
#print 100 to 1 numbers

for i in range(100,0,-1):
 print(i)



# 3rd question
# print multiplication table of n number

n= int(input("Enter the no :"))
for i in range(1,11):
    print(i*n)



n=5
for i in range(1,n+1):
    sum = sum + i
    print(sum)






