#Tuple: Tuple is a Collection datatype, which is used to multiple values in a single variable.
       #Tuple is ordered , Immutable and also allows the duplicate values and can store the mixed data types in values.

#Example :
coordinates = ("x","y")
My_tuple = (10,20,30)
print(My_tuple)
print(type(My_tuple))

# Creating a Tuple:
# Empty tuple
Et = ()
# Tuple with numbers:
N = (1,2,3,4,5,6)
# Tuple with strings:
s = ("A","B","C","a","b","c")
# Tuple with mixed datatypes:
M = (24,3.14,"A","c",True,"False")
# Tuple with single Element:
a = 10 # int
print(type(a))
b = [10] #list
print(type(b))
c = (10,) # tuple
print(type(c))

# Accessing Elements:
# Tuples uses index values to access an element.
A = (10,20,30,40)
#i    0  1  2  3
#-i  -4 -3 -2 -1
print(A[0]) # 10
print(A[1]) # 20
print(A[2]) # 30
print(A[3]) # 40
print(A[-1]) # 40
print(A[-2]) # 30
print(A[-3]) # 20
print(A[-4]) # 10

# Slicing the tuple:
# Extracting part of the tuple using start index and end index.
# ([Start index : End index])
A = (10,20,30,40)
#i    0  1  2  3
#-i  -4 -3 -2 -1
print(A[1:3]) # 20 30
print(A[:2]) # 10 20 
print(A[-3:-1]) # 20 30
print(A[:]) 

# Changing the Values:
# Tuples are immutable, So we cannot change the values.
# #TypeError: 'tuple' objects does not support item assingment
# append():
# A.append(50)
# print(A)

# Lenght:
print(len(A))
# max:
print(max(A))
# min:
print(min(A))
# sum:
print(sum(A))
# Concatenation:
x = ("hyderabad","yadgir")
y = ("waragal","Mbnr")
z = x+y
print(z)
# Repeatation:
a = "227"
print(a*3)
 
# Searching and Checking:
x = ("shiva","pradeep","pual")
print("shiva" in x)
# in operator:
# not in operator:
# index():
print(A[2])
# count():
# Sorting and Reversing:
# Iterating tuple using for loop: