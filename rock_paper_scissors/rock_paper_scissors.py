#   Python Rock Paper Scissors Game
#   Tuple - good choice since options won’t change

import random

options = ("rock", "paper", "scissors")
running = True

print("Aloha! Fancy a game of Rock, Paper, Scissors?")

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Let's go! Rock, Paper, Scissors? ").lower()

    print(f"Player chooses {player}.")
    print(f"Computer chooses {computer}.")

    if player == computer:
        print("Like kissing your sister - It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Not bad at all! A win for you.")
    elif player == "paper" and computer == "rock":
        print("Not bad at all! A win for you.")
    elif player == "scissors" and computer == "paper":
        print("Not bad at all! A win for you.")
    else:
        print("Too bad!! The computer rules this game!")

    if not input("Would you like to play again? (y/n) ").lower() == "y":
        running = False

print("Thank you for playing!\nMahalo")
