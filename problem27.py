#Check if a number is positive, negative, or zero.

number = int(input("Enter your number: "))

if number < 0:
    print(f"{number} is negative.")
elif number == 0:
    print(f"{number} is zero.")
else:
    print(f"{number} is positive.")