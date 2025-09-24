# Sets: 
# Set is collection datatype which is used to store multiple values in a single variable.
# sets are unordered , unindexed , mutable , and they do not allow duplicate values.
# They are useful when you want to store unique elements and performs the mathematical operators like union , intersection and difference.
# Syntax:
# My_set = {element1,element2,element3} 
# Characteristics of the Sets:
# Unordered:
# example: {1,2,3} and {3,2,1} are considered the same set.
# Unindexed: You cannot access set elements by the index like lists or tuple. set[1]
# a = {1,2,3}
# print(a[1])-> Error
# Unique values only: It automatically removes duplicate values.
a = {1,2,3,3,2,1,1,1,2}
print(a)
# Empty set
s1 = {}
print(s1)
print(type(s1))
s2 = set()
print(s2)
print(type(s2))
# Accessing sets:
# we cannot directly access an element using index but we access an element using loops.
Coolie = {"Rajinikanth","Snake king","upendra"}
for role in Coolie:
    print(role)

# Adding an element in sets:
S = {12,18,20}
S.add(25) # adds only single element in any position
S.update([34,29]) # adds the multiple values in the set
print(S) # {12,18,20,25,34,29,}
  
# Deleting the elements in set:
# remove(): Removes the element,but it gives an error if the value is not found in the set.
S = {12,18,20,25,34,29,25}
S.remove(25)
print(S)













# Mathematical Operations in set:
# Union "U"="|": Prints all unique values or elements from the both sides.
A = {1,2,3}
B = {4,5,6}
print(A | B) # {1,2,3,4,5,6}
# Intersection "∩" = "&" : Prints the common elements from the set.
A = {1,2,3,4}
B = {3,4,5,6}
print(A & B) # {3,4}
# Difference "-" = "-": removes the common elements from the lists but prints only the first sets values.
A = {1,2,3,4}
B = {3,4,5,6}
print(A - B) # {1,2}
print(B - A) # {5,6}
# Symmetric difference "Δ" = "^"
A = {1,2,3,4}
B = {3,4,5,6}
print(A ^ B)

# Mathematical operations using functions:
A = {1,2,3,4}
B = {3,4,5,6}
# Union
print(A.union(B)) # {1,2,3,4,5,6}
# Intersection 
print(A.intersection(B)) # {3,4}
# Difference
print(A.difference(B)) # {1,2}
# Symmetric difference
print(A.symmetric_difference(B)) # {1,2,5,6}

# len():
S = {11,22,33,44,55,66}
print(len(S)) # 6
# max():
S = {11,22,33,44,55,66}
print(max(S)) # 66
# min():
S = {11,22,33,44,55,66}
print(min(S)) # 11
# sum():
S = {11,22,33,44,55,66}
print(sum(S)) # 231
# sort():
S = {11,22,33,44,55,66}
print(sorted(S))
S = {11,22,33,44,55,66}
S.reverse()
print(S)