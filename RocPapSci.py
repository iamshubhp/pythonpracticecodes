# Rock Paper Scissor game in Python

import random

options = ("rock", "paper", "scissor")

running = True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice between Rock, Paper, Scissor: ").lower()

    print(f"Player: {computer}")
    print(f"computer: {player}")

    if player == computer:
        print("it's a Tie")
    elif player == "rock" and computer == "scissor":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer == "paper":
        print("you win!")
    else:
        print("you loose!")

    if not input("Play again? Y/N : ").lower() == "y":
        running = False

print("Thanks for playing!")
