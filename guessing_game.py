import random
import sys

def welcome():
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print("Rules:")
    print("Guess a number between 1 and 100")
    print("Try to guess within 10 attempts")
    print("Type 'quit' to exit.")
    print("Good Luck!")

def user_guess():
    ui=input("\nEnter your guess:")
    if ui.lower()=="quit":
        return None
    try:
        guess = int(ui)
        if 1<=guess<=100:
            return guess
        else:
            print("Please enter a number between 1 and 100")
    except ValueError:
        print("Invalid input! Please enter a number or type 'quit' to exit.")

def play():
    secret=random.randint(1,100)
    attempts=0
    max_attempts=10
    print("I've picked a numnber between 1 and 100!")
    print(f"You have {max_attempts} attempts to guess it right!")
    while attempts<max_attempts:
        guess=user_guess()
        if guess is None:
            print("Thanks for playing, goodbye!")
            return
        attempts+=1
        rem=max_attempts-attempts
        if guess==secret:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            print(f"The number was {secret}")
            print(f"Your score: {100-(attempts*2)}%")
            return
        elif guess<secret:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")
    print(f"Game over!You've used all {max_attempts} attempts!")
    print(f"the number was {secret}")

def main():
    welcome()
    while True:
        play()
        while True:
            play_again=input("Would you like to play again? (y/n)")
            if play_again.lower()=="y":
                play()
                break
            elif play_again.lower()=="n":
                print("Thanks for playing, goodbye!")
                sys.exit()
            else:
                print("Please enter 'y' for yes or 'n' for no")

if __name__ == "__main__":
    main()