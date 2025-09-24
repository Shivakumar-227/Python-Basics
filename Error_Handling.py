# Error Handling:
# -> Errors are mistakes in a program that stop it from working correctly.
# -> Exception is a special type of error that occurs while the program is running.
# -> python provides ways to handle exceptions so that the program doesn't crash suddenly.
# -> Types of error:
# 1.Compile-time Error: (Syntax Error)
# Errors that happen when the code is not written correctly(wrong syntax)
# 2.Logical Error:
# Error when the program runs but gives wrong output because the logic is wrong.
# 3.Runtime Error: (Exceptions)
# Errors happens when the program is running.

# Types of exception in python:
# 1. ZeroDivisionError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. TypeError
# 6. FileNotFoundError

# 1. ZeroDivisionError:
# It is an exception which divides a number by zero.
# try:
#     a = int(input("Enter the numerator: "))
#     b = int(input("Enter the Dinominator: "))
#     c = a//b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Divisor by zero is not possible")
# try:
#     a = int(input("Enter the numerator: "))
#     b = int(input("Enter the Dinominator: "))
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Divisor by zero is not possible")
try:
    i = 3
    n = int(input("Enter the value: "))
    if i%n == 0:
        print("Yes , number is multiple of,n")
    else:
        print("No , number not is multiple of,n")
except ZeroDivisionError:
    print("Error: division by zero is not possible")
              