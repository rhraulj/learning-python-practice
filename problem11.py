# Rock , paper , scissors

print("\nPlayer 1 and Player 2 please choice with this list to star the game.")
print("Rock,Paper,Scissors")
print("________________________")

player1 = input("Player 1 enter your choice: ")
player2 = input("\nPlayer 2 enter yuor choice: ")


if player1 == "Rock" and player2 == "Rock":
    print(f"{player1}, {player2} you both win!")
elif player1 == "Rock" and player2 == "Paper":
    print(f"{player2} you are winner!")
elif player1 == "Rock" and player2 == "Scissors":
    print(f"{player1} you are winner!")
elif player1 == "Paper" and player2 == "Rock":
    print(f"{player1} you are winner!")
elif player1 == "Paper" and player2 == "Paper":
    print(f"{player1}, {player2} you both win!")
elif player1 == "Paper" and player2 == "Scissors":
    print(f"{player2} you are winner!")
elif player1 == "Scissors" and player2 == "Rock":
    print(f"{player2} you are winner!")
elif player1 == "Scissors" and player2 == "Paper":
    print(f"{player1} your are winner!")
elif player1 == "Scissors" and player2 == "Scissors":
    print(f"{player1}, {player2} you both win!")
else: 
    print("Invalid input. Please choose Rock, Paper, or Scissors.")