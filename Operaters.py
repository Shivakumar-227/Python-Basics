









#Comparision or Relation Operator
x = 5
y = 8
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
#Logical operators
#AND
p = 5
q = 10
print(p>2 and q>5)
print(p>2 and q<5)
print(p<2 and q>5)
print(p<2 and q<5)
#OR
p1= 5
q1= 10
print(p1>2 or q1>5)
print(p1>2 or q1<5)
print(p1<2 or q1>5)
print(p1<2 or q1<5)
#NOT
p2 = 5
q2 = 0
print(not(p2))
print(not(q2))
#Assignment operator
a1 = 10
a1 += 1
print(a1)
a1 -= 1
print(a1)
a1 *= 2
print(a1)
a1 /= 2
print(a1)
a1 //= 2
print(a1)
a1 **= 2
print(a1)  
#Bitwise operator
x = 5
y = 2
print(x & y)
print(x | y)
print(~x)
print(x ^ y)
print(x << y)
print(x >> y)
#identity Operators #executes for whole list
x = [1,2,3,4]
y = x
z = [1,2,3,4]
print(x is y)
print(x is z)
print(x == z)
print(x is not z)
print(y is not z)
#Membership operators #executes in squence order
text = [1,2,4,5,6,9]
print(9 in text)
print(4 not in text)
print(0 not in text)
print(100 in text)
