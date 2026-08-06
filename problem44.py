# Print a multiplication table for a number the user provides.

num = int(input("Enter number: "))

i = 1
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1