#This file contains the code for the advanced Mathematics calculations

print("--------------------------------")
print("Here you are going to experience with advanced Mathematics")
print("--------------------------------")
print("Plus, you are going to do this by yourselves...")

number1 = input("Enter the first number : \n")
number2 = input("Enter the second number : \n")

def sum(a, b):
    return a+b
def substract(a, b):
    print(a-b)
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b == 0:
        return "This operation is not supported"
    return a/b

print("Choose the operation you wish to perform")

choices = {"1":"Addition", "2":"Substraction", "3":"Division", "4":"Multiplication"}


for x,y in choices.items(): 
 print(x,y)

choice = input("Choose one option : ")
print("Your choice is : "+choice)

def treatChoice(choice):
    print(choice)
    
    if choice==1:
       return sum(number1,number2)
    elif choice==2:
       return substract(number1,number2)
    elif choice==3:
       return multiply(number1,number2)
    elif choice==4:
       return divide(number1,number2) 
        
print("--------------------------------\n")
print("The result of that operation is %s : " %treatChoice(choice))

print("-------------  Thank you so much!!! ------------------- \n\n")

print("October inspiration")