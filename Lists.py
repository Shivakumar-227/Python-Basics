
x = ["10","20","30","40","50"] # integer values
fruits = ["apple","banana","mango"] #string values
list2 = [10.1,20.2,30.3,40.4,50.5] #float values
list3 = [True,False,True] #boolean values
list4 = [10,20.5,"hello",True,"flase"] # multiple data types
print(x)
print(fruits)
print(list2)
print(list3)
print(list4)
# indexing lists
x = ["10","20","30","40","50"] # integer values
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
# by negative indexing
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
# Slicing in lists
# slicing is taking out of a part from the main list.
# slicing will extracts the part or sublist using [start idx : end idx]
# example:
slc1 = ["prabhas","balayya","pspk","bob","bhai"]
print(slc1[1:3])
print(slc1[1:4])
print(slc1[-3:])
#adding Elements in list:
#we can add new values to a list in different ways:
#1. Append:Adds a single value at the end of the list.
KalkiCast = ["Prabhas","Kamal h","Amitha Bhachan","Deepika P","SSR"]
print(KalkiCast)
KalkiCast.append("Deesha patani")
print(KalkiCast)
# 2.Insert: Adds a single value at the particular position using index
KalkiCast.insert(2,"Vijay D")
print(KalkiCast)
# 3.Extending : Adds a multiple values at once by combining the lists 
KalkiCast.extend(["Anudeep","Mrunal T","bujji"])
print(KalkiCast)
#add bhramanandham
KalkiCast.insert(5,"bhramanandham")
#Removing Elements in list
#Removing the items in the list in different ways
#1. remove(): Removes or deletes the first occurrence of the specific items
KalkiCast.remove("Mrunal T")
print(KalkiCast)
#2. pop(): deletes the items from list at the particular position
KalkiCast.pop(6)
print(KalkiCast)
#3. clear(): Deletes the all items from the list
KalkiCast.clear()
print(KalkiCast)

# Changing the Elements:Lists are mutable,we can change the values after creating the lists using index
#KalkiCast[1] = "Sandeep R V"
print(KalkiCast)
# Mathematical OPerators in lists
# 1. Concatenation: joins the two lists together in one list
# a = [1,2]
# b= [3,4]
# c = a+b
# 2. repeatations the elements of a list multiple times 
# a = [1,2]
# n = int(input("Enter a value"))
# b = a * n
# print(b)
#Searching and Checking:
# we can check if an element or values exists in a list or not.
#In operator:
#It is a membership operator , which returns the true values if the elements is exists in the lists.
a = [2,4,6,8,10,12,14]
if 2 in a:
    print("Yes item is present in the list")
#not in operator:
#It is a membership operator , which returns the true values if the elements is not exists in the lists.
b = [2,4,6,8,10]
if 3 is not b:
    print("No item is present in the list")
# Index(): Which gives the position of the first occurance of an element or value.
print(a.index(8))

# count (): Which gives the  number of the elements in the list 
a = [2,4,6,8,10,12,14]
cnt = 0
print(a.count(8))
for a in range(10):
    if a == 8:
        cnt = cnt + 1
print(cnt)

# Sorting: sort()
# It arrange elements  either in ascending order (small to large) or descending order (large to small).
# It flips the list so the last element will become the first element.
st = [25,12,5,31,13,18,7,45,55,68]
# AO = [5,12,13,18,25,31,45,55,68]
st.reverse()
print(st)
# DO = [68,55,45,31,25,18,13,12,5]
st1 = [25,8,4,7,10] # 25,10,8,7,4
st1.sort(reverse=True)

("1 5 4 2 3")
# R = 3 2 4 5 1 # Ao = 1 2 3 4 5
# Ao = 1 2 3 4 5

# Copying the list:
# Copying creates a new list with the same element, so changes in the new list do not affect the original list.
Frd1 = ["A","B","C","D","A","D","B","B","C","C","A","A"]
Frd2 = Frd1.copy()
Frd2[2] = "B"
print(Frd2)

# Built-in Function with loops:
# Python programming provides many ready-made functions to work
st = [25,12,5,31,13,18,7,45,8,55,68]
st.sort()
# len(): Returns the number of elements.
print(len(st))
# max():Returns the maximum element from the list.
print(max(st))
# min():Returns the minimum element from the list.
print(min(st))
# sum():Returns the total sum of all numeric elements.
print(sum(st))

# a = "hello world to the python programming"
# b = a.split()
# print(b)
# # Multiple values using input data to the list:
# a = (map(int,input("enter the multiple values:").split())) #10 20 30 40 50 
# a.sort()
# print(a) #[10,20,30,40,50] #integer values 

# b = input("enter the multiples values")
# a = (map(int,input("enter the multiple values:").split())) #10 20 30 40 50 
# a.sort()
# print(a) # ['10','20','30','40','50']#integer values

# b = input("enter the values:").split() # 10 20 30 40 50 
# print(b) #['10','20','30','40','50'] # string values

#Traversing a list:
# Accessing the elements using a loop
# using for loop 
cars = ["thar","jaguar","Audi","bmw"]
print(len(cars))
# index   0        1       2     3
for car in range(0,4):
    print("cars",car)

#Using index with for loop:
a = len(cars)  #4
for i in range(0,a):
    print("cars",i,cars[i])

# Adding elements using for loop:
# list = "thar","jaguar","audi","bmw"
# list = []
# for i in range(0,5):
#     a = input("Enter the values: ")
#     list.append(a)
# print(list)

# list = []
# for i in range(0,8):
#     a = input("Enter the name: ")
#     list.append(a)
# print(list)

# Give the input values to the lists from 1 to 10
# list = []
# n = int(input("Enter the number of list values: ")) # 10
# for i in range(n): # i 1 2 3 4 5 6 7 8 9 10
#     list.append(i)
# print(list)

# sum of lists items = 10 20 30 40 50 without using sum().

list = [10,20,30,40,50,]
sum = 0
for i in list: # 0 1 2 3 4
    sum = sum + i
print(sum)

# convert ["p","y","t","h","o","n"] to python
list1 = ["y","t","h","o","n"]
word = "p"
for i in list1: # y t h o n
    word = word + i
print(word)
max() 
# Find the Maximum and Minimum number from list without using max() and min().

list1 = [7,18,12,31,45,17,10,23,229,227] # Max = 229 # Min = 7
list1.sort()
# [7,10,12,17,18,23,31,45,227,229]
#  0  1  2  3  4  5  6  7  8   9
print("Maximum of list :",list1[9])
print("Minimum of list :",list1[0])

# Finding the maximum and minimum number from list without using max(),min(), sort().
list1 = [52,7,18,12,31,45,17,10,23,229,227]
max = list1[0] # 229
min = list1[0] # 7
for num in list: # [52,7,18,12,31,45,17,10,23,229,227]
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num
        
print(max1)
print(min1)
# Searching for an element in a list.
Names = ["Malla reddy sir","Revanth reddy","Modi sir","KCR Sir","Rahul Gandhi"]
Searching_name = input("Enter the name to be found: ")  # modi # kcr
found = False 
for i in Names:
    if Searching_name == i:
        found = True

if found:
    print("Yes")
else:
    print("No")

# Count even and odd numbers
numbers = [7,10,12,17,18,23,31,45,227,229]

evn_cnt = 0
odd_cnt = 0
for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        evn_cnt += 1
    else:
        odd_cnt += 1
print("Number of even numbers are: ", evn_cnt)
print("Number of odd numbers are: ", odd_cnt)

# Reversing a list without reverse 
list1 = [7,10,12,17,18,23,31,45,227,229]  
# ind =   0 1  2  3  4  5  6  7  8   9
l = len(list1)
r_list = []
for i in range(l-1,-1,-1):
     r_list.append(list1[i])
print(r_list)

# Removing all negative numbers using loop
numbers = [-56,-9,-8,-30,30,45,23,-19,72,-55,-18,7,0]
positive_list = []
for i in range(len(numbers)):
     if numbers[i] > 0:
          positive_list.append(numbers[i])
print(positive_list)


# Multiply each element in the list
numbers = [56,92]