#Possitive , Nagative , Zero

number = int(input("Enter number: "))

if number == 0:
    print("Zero!")
elif number >= 0:
    print("This is Positive number.")
elif number <= 0:
    print("This is Nagative number.")
else:
    print("Please Enter a valid number.")