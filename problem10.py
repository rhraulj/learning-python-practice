# Movie ticket Calculator

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <= 12 :
    print(f"{name} your payment is $5.")
elif age < 65:
    print(f"{name} your payment is $12.")
else:
    print(f"{name} you are senior citien criteria, amount is $7.")