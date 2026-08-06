# Write a program using functions to greatest to three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def greatestNumber():
    if a > b and a > c:
        print("First number is greatest number.") 
    elif b > a and b > c:
        print("Second number is greatest number.")
    elif c > a and c > b:
        print("Third number is greatest number.")
    else:
        print("Sorry") 

greatestNumber()

