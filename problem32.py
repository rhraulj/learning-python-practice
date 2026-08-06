#Print the multiplication table of a given number (1 to 10).

number = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(f"{number} X {i} = {number * i}")
    i += 1