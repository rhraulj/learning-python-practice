# Voting eligibility (18+)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18: 
    print(f"Congratulations! {name} \nYour are aligibale for voting. Age: {age}")
else:
    print("Sorry you are not 18 yet for voting.")