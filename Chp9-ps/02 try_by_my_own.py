import random

def game():
    print("You are plaing a game..")
    score = random.randint (1,50)

    #Fetch the hiscore1

    with open("hiscore1.txt") as f:
        hiscore1 = f.read()
        if(hiscore1!=""):
            hiscore1 = int(hiscore1)
        else:
            hiscore1 = 0

    print(f"Your score: {score}")
    if(score>hiscore1):
        #write the hicore1 to the file 
        with open("hiscore1.txt", "w") as f:
            f.write(str(score))
    return score
game()