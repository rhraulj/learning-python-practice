# Simple grading system: 90+ = A, 75-89 = B, 50-74 = C, below 50 = Fail.

grade = float(input("Enter your grade: "))

if grade >= 90:
    print("You got an A.")
elif grade >= 75:
    print("You got a B.")
elif grade >= 50:
    print("You got a C.")
else:
    print("You failed.")