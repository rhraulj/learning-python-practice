# Given a 3-digit number, extract and print each digit separately (using // and %).

number = int(input("Enter a 3-digit number: "))

hundreds = number // 100
print(f"Hundreds digit: {hundreds}")

tens = (number // 10) % 10
print(f"Tens digit: {tens}")

units = number % 10
print(f"Units digit: {units}")