# Take two numbers as string input, add them as numbers, then concatenate them as strings, and print both results to see the difference.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Adding as numbers
sum_as_numbers = int(num1) + int(num2)

# Concatenating as strings
concat_as_strings = num1 + num2

print(f"Sum as numbers: {sum_as_numbers}")
print(f"Concatenated as strings: {concat_as_strings}")
