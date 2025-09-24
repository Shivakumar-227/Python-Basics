i = 0
while i<10:
    print(i)
    i += 1

# Printing Even numbers 0 to 20
i = 0
while i<21:
    print(i)
    i += 2

#printimg Square upto 6
i = 1
while i<=6:
    print("square of",i,"=",i**2)
    i += 1

#5 table
i = 1
while i<=10:
    print("5 x",i,"=",5*i)
    i += 1

#6 table
i = 1
while i<=10:
    print(f"6 x {i} = {i*6}")
    i += 1
# 1+2+3+4+......25 = ?
i=1
sum=0
while i<=25:
    sum=sum+i
    print(sum)
    i += 1

#factorial of 4
i = 1
product=1
while i<=4:
    product=product*i
    print(product)
    i+=1

# breaking at some point
i = 1
while i<=25:
    print(i)
    if i == 15:
        break
    i += 1 

# continue condition
i = 1
while i<26:
    i += 1
    if i == 15:
     continue
    print(i)