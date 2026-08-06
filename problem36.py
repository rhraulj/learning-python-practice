# Check if a number is even or odd using the modulo operator (no if-statement — just print True/False).

number = int(input("Enter a number: "))
is_even = (number % 2 == 0)
print(f"{number} is even: {is_even}")