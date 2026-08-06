# Variables, Data type & \oparetors.

#Take a person's name and age as input, print: "Hi <name>, you'll turn 100 in <year>."

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = int(input("Enter current Year: "))

current_age = current_year - year_of_birth
year_turn_100 = current_year + (100 - current_age)

print(f"Hi {name}, you'll turn 100 in {year_turn_100}.")