# Computer picks a random number between 1–100.
# - User keeps guessing until correct.
# - After each guess, tell them "Too high" or "Too low".
# - Count and display number of attempts.
# - Ask if they want to play again.
# - **Validate input** — don't crash if user types letters instead of a number.


import random

def play_game():
    secret = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

main()