#This code is for practicing the basics of Python

import math

#This code print the Hello World! message
print("Hello, World!")

# This is a method declaration in Python that calcultes the sum of two numbers and prints their sum 
def add(a,b):
 return a + b

print("Hello, World! The sum is %s" % add(1,5))

#This is the code to ask for user input in Python
name = input("What is your name? \n")
print("Welcome Mr. "+name) #This prints the name entered by the user
print("The length of your name is: "+str(len(name))) # This prints the length of the name entered by the user

#Method for multiplication of two numbers
def multiply(a,b):
    return a * b
print("Muliplication of these two numbers is %s " %multiply(52,36)) # This prints the muliplication of thse 2 numbers

#Method for the division of two numbers
def divide(a,b):
    if a == b:
        return 1
    elif b==0:
        return "This operation is impossible"
    elif b!=0:
        return a/b
    
print("Division of these two numbers is %s " %divide(58,2)) # This prints the division of thse 2 numbers    

# Method to calculate the remainder of two numbers 
def remaining(a,b):
    return a%b
print("The remainder of this division %s is " %remaining(7,2))

#Calculate the square root of a number
def squareRoot(a):
    return math.sqrt(a)
sqrt1 = squareRoot(55)
sqrt2 = squareRoot(5)
print("The square root of these two numers %s is : " %sqrt1 +" and %s" %sqrt2) #

#Calculate the square root of a number
def square(a):
    return a**2
sq1 = square(55)
sq2 = square(5)
print("The square of these two numers %s is : " %sq1 +" and %s" %sq2) #
