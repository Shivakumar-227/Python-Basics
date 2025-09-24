# File open ("file name","mode") # r,w,a,rb,wb,r+,w+
file = open("student.txt","r")
print("file created")
file.close()
# Types of Read():
# 1. read() =>
file = open("student.txt","r")
content = file.read()
print(content)
file.close()
# # 2. readline() =>
# file = open("student.txt","r")
# content = file.readline() # 1st line
# content1 = file.readline() #2nd line
# content2 = file.readline() # 3rd line
# print(content)
# print(content1)
# print(content2)
# file.close()
# # 3. readlines() =>
# file = open("student.txt","r")
# content = file.readlines()
# print(content)
# file.close()