# The Secret Number Game


sec_num = 50

while True:
    guess_num = int(input("Enter a number: "))
    if guess_num > sec_num:
        print("Too high!!")
    elif guess_num < sec_num:
        print("Too Low!!")
    else:
        print("You Win!!")
        break