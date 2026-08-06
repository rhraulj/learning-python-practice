# Use a `while` loop to keep asking the user for a password until they type "correct".

password = ""
while password != "Rituraj":
    password = input("Please enter the password: ")
    if password != "Rituraj":
        print("Incorrect password, please try again.")