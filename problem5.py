# Grade calculator

name = input("Enter student name: ")
marks = int(input("\nEnter your marks: "))

if marks >= 90: 
    print(f"\n{name} Congratulations! Your Grade is A ")
elif marks >= 75:
    print("\nYour grade is B")
elif marks >= 60:
    print("\nYour grade is C")
elif marks >= 34:
    print("\nYour grade is D")
else:
    print("Sorry Failed!!")