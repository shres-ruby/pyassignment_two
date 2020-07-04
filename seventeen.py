# 17. Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. 
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors. 

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise Exception("Zero division error. Please enter a positive denominator")
    return x/y

num1 = int(input("Please enter a number : "))
num2 = int(input("Please enter another number : "))

print("Please select an operation : ")
print("Enter number 1 for addition | Enter number 2 for subtraction | ")
print("Enter number 3 for multiplication | Enter number 4 for division |")

op = int(input("Please enter a number : "))
if op not in range (1,5):
    raise Exception("Please enter a number between 1 and 4")

if op == 1:
    result = add(num1,num2)
    print(f"The sum of {num1} and {num2} is {result}")

elif op == 2:
    result = subtract(num1,num2)
    print(f"The difference between {num1} and {num2} is {result}")

elif op == 3:
    result = multiply(num1,num2)
    print(f"The product between {num1} and {num2} is {result}")

else:
    result = divide(num1,num2)
    print(f"{num1} divided by {num2} is {result}")