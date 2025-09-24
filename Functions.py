# Functions:
# A function is a block of code that performs a specific task.
# It allows us to group instructions together and reuse them whenever we needed.
# Instead of writing the same code again and again, we just define a function once and call it whenever required.
# Syntax:
## Functions:
# A function is a block of code that performs a specific task.
# It allows us to group instructions together and reuse them whenever we needed.
# Instead of writing the same code again and again, we just define a function once and call it whenever required.
# Syntax:
# def function_name(parameters):
#     # function body cade
#     return value # optional
# function_name()
# # example:
# def greet():
#     print("Hello World!")

# Calling a Function:
# Calling a Function means telling python to run the code inside a function by using it's name followed by paranthesis().
# If the function needs the input (paramter), We peovide values (argument) inside the paranthesis.
# When we call a function, python jumps to the function, excutes it's code, and then comes back to continue the program.
def greet(name,branch): # function name
    print("Hello World!",name,branch) #
    greet("Shiva","CSE-AI&ML") # calling a function.

# Passing Parameters & Arguments.
# Parameters: A variable declared inside the function defintion.
# It's act like an empty container waiting to receive a value.
# Arguments: The actual value we pass into the function when calling it. It fills the empty container(Parameter).
# Example:
def greet(name):
    print("Hello",name)
greet("Shiva")
# Same task without function.
name = "Shiva" # Here name is input variable(Parameter), and "Nandhan" is value to the parameter(Argument).
print("Hello",name)

# Types of Functions Arguments:
# A. Positional Arguments:
# When we pass Arguments in the same order as the function parameter, they are called positional Arguments.
# Here the order(position) is very important.
def greet(name,rollno): # step 2 values store
    print("Hello",name,"your rollno is" ,rollno) # step3: excute the line
greet("Shiva","E7") # step1: function calling

# B. Keyboard Arguments:
# When we pass values or Arguments by writing the parameter(variable = value), they are called as keyboard Arguments.
def greet(rollno,name):
    print("Hello",name,"your rollno is" ,rollno)
greet(name="Shiva",rollno="E7")

# C. Default Arguments:
# When a parameter has default value(assigning the value in parameter) in the function definition, it becomes a default argument.
def greet(name="student"):
    print("Hello",name)
greet()
greet("Shiva")

# D.Variable-length Arguments:
# Sometimes we don't know how many arguments will be passed to a function.
# python provides two special ways to handle this:
# 1. *args:(Variable-length Arguments):
# collects multiple values into a tuple.
# l = 10,20,30,40,50
def sum1(*List1):
    sum2 = 0
    for i in range(len(List1)):
        sum2 = sum2 + List1[i]
    print(sum2) #150
    print(type(List1))
sum1(10,20,30,40,50)

# 2. **kwargs:(Keyworded Variable-length Arguments):
# Collect multiple key=value pair into a dictionary.
def details(**info):
    for i,j in info.items():
        print(i,":",j)
details(Name="shiva",Rollno="E7",Branch="CSM") 

# Scope of the variable:
# Scope of the variable:
# The scope of a variable means the part of the program where that variable can be accessed or used.
#In python, variables can be local and global, depending on where they are created.
# Local variable.
# A variable declared inside a function is called a local variable.
# It exists only while the function is running.
# Global variable.
# A variable declared outside that function is called a global variable.
# It can be accessed anywhere in the program(inside or outside functions).
x = 10 # Global variable
def var1():
    y = 5 # Local variable
    print("inside var1 function",x,y)
var1()
def var2():
    print("inside var2 function",x,y)
var2

print("outside function",x)

# Lambda fuction:
# normal function
def sqe(a):
    print(a*a) # 25
sqe(5)
# Lambda function:
squ = lambda a:a*a
print(squ(5))