#Write a program that categorizes a number as negative, zero, or positive.

number = int(input("Enter yuor number: "))

if number < 0:
    print(f"{number} is negative.")
elif number == 0:
    print(f"{number} is zero.")
else:
    print(f"{number} is positive.")
