# Dictionary:
# Dictionary is a in-build datatype which is used to store multiple values in a single variable.
# -> Dictionary stores the data in the form of key-value pairs.
# -> Each is unique and works as an index to access its corresponding value.
# Keys are immutable(can't be changed once created), while values can be anything(mutable).
# Dictionary are: Ordered(From python 3.7+ version), Mutable, Do not allows the duplicate keys.
# Syntax:
My_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print(My_dict)
# Characteristics of Dictionaries:
# Key-value pairs:
# Every entry of Dictionary's element is a pair: keys and values.
# { "name":"nandhan"}
# unique keys:
# Example:
A = {"n":"Shiva", "n":"nandhan"}
print(A) # "n":"shiva"
# keys must be immutable:
# keys can be(valid keys): Integers,float,string.
# Example:
My_dict = {
    1:"value1",
    10.2:"value2",
    "key3":"value3",
    "key4":"value4"
}
print(My_dict)
# Creating Dictionary:
# Normal Dictionary:
BioData = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad"
}
print(BioData)
# Dictionary using Constructor:
BioData1 = dict( Name="Shiva",RollNo = "E7",Branch = "CSE AI&ML",Place = "Hyderabad")

# Empty dictionary:
E_D = {}

# Accessing a dictionary:
# To access an element we use keys name inside the square brackets[] or we can use get() method.
# Example:
Biodata = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad"
}
# Square brackets[]:
print(BioData["Name"]) # Shiva
print(BioData["Roll.No"]) # E7
print(BioData["Branch"]) # CSE AI&ML
print(BioData["Place"]) # Hyderabad
#print(BioData["Age"]) -> key error(Because the age is not created in dictionary)

# Using get() method:
print(BioData.get("Name"))
print(BioData.get("Roll.No"))
print(BioData.get("Branch"))
print(BioData.get("Place"))
print(BioData.get("Age")) # None instead of error

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pair into a dictionary.
# Updating: You can update or change the values using existed keys in the dictionary.
BioData = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad"
}
BioData["age"] = 18 # Adding the key and values
print(BioData)
BioData["Place"] = "Narayanapet" # Changing or updating the existed key's and value.
print(BioData)

# Removing in Dictionary:
# Python gives multiple ways to deleted items from a dictionary.
# pop(),pop item(),clear(),del(delete)
BioData = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad",
    "Role":"Under graduate"
}
#pop(): Removes the key value.
BioData.pop("Roll.No")
print(BioData)
#popitem(): Removes the last inserted item from the dictionary.
BioData.popitem()
print(BioData)
#del(delete): Deletes the keys from dictionary.
del BioData["Branch"]
print(BioData)
#clear(): Removes every item from the dictionary.
BioData.clear()
print(BioData)

# Dictionary methods:
# Methods allow you to access dictionary data easily.
BioData = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad",
    "Role":"Under graduate"
}
# keys(): It prints only the keys of dictionary
print(BioData.keys())
# values(): It prints only the values of dictionary
print(BioData.values())
# items(): It prints both keys and values
print(BioData.items())

# Updating update(): update the multiple values
BioData.update({"Role":"Web Developer","Place":"Hyderabad"})
print(BioData)

# Loops for Dictionary:
L = [10,20,30,40,50]

for i in L:
    print(i)
    
BioData = {
    "Name":"Shiva",
    "Roll.No":"E7",
    "Branch":"CSE AI&ML",
    "Place":"Hyderabad",
    "Role":"Under graduate"
}
# Loops to iterate the key (by default the Dictionary's will stores the keys value.):
for i in BioData:
    print(i)
# Loops to iterate the keys using keys() method:
for i in BioData.keys():
    print(i)
# Loops to iterate the values using values () method:
for i in BioData.values():
    print(i)
# Loops to iterate the item using items() method:
for i in BioData.items():
    print(i)

# Nested Tuple:
T = (10,(20,30),(40,50))
#i    0    1       2
print(T[2][1])

# Nested Dictionary:

Students = {
    "S1":{"Name":"Shiva", "RollNo":"E7"},
    "S2":{"Name":"Pradeep", "RollNo":"F9"},
    "S3":{"Name":"Pual", "RollNo":"E8"}
}
print(Students["S1"]["Name"])
print(Students["S2"]["RollNo"])
print(Students["S1"]["RollNo"])
print(Students["S2"]["Name"])
print(Students["S3"]["Name"])