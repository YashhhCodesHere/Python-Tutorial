import random

choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

name = input("Enter your name: ")
userInput = input(f'''\nHey {name}!
(Rules are:- Press 'R' for Rock, 'P' for Paper, & 'S' for Scissors)\n 
Please enter your choice: ''').lower()

Inputs = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

if userInput in Inputs:
    user = Inputs[userInput]
    print(f"\nComputer chose: {computer}")
    print(f"You chose: {user}")

    if computer == user:
        print("Game is Draw!")
    else:
        if (computer == "Rock" and user == "Paper") or \
           (computer == "Paper" and user == "Scissors") or \
           (computer == "Scissors" and user == "Rock"):
            print("\nYou Win!")
        else:
            print("\nComputer Wins!")
else:
    print("Invalid input! Please enter 'R', 'P', or 'S'.")
