# Loop is a program
#  for variable in seq:
#   code block
# range(start v(0),end v, step v )
for i in range(1,6,1):
    print("hello")

#Print the numbers from 9 to 27
for a in range(9 , 28):
    print(a)

# Using default values print the numbers upto 15.
for a in range(16):
    print(a)

# 10,9,8,7,...1
for i in range(10,0,-1):
    print(i)
    
# Print the even numbers from 0 to 20
for k in range(0,21,2):
    print(k)

#  print squares of a number upto 6
for i in range(1,7):
    print(i**2)

fruits = ["apple","mango", "banana"]    
for fruit in fruits:
    print(1)

fruits = "apple"
for i in fruits:
    print(i) 

# 5 table
for i in range(1,11):
    print("5 x",i,"=",5*i)

 # 7 table
for i in range(1,11):
    print("7 x", i ,"=",7*i)

#  1+2+3+5+........+25
sum = 0
for i in range(1,26):
    sum=sum+i
    print(sum)

# Factorial of 4
product=1
for i in range (1,5):
    product=product*i
    
# breaking at some point
for i in range(1,25):
    print(i)
    if i == 7:
     break 

# continue  
for i in range(1,26):
    if i == 6:
        continue
    print(i)

for i in range(1,30):
    if i%2==0:
        pass
    else:
     print(i)