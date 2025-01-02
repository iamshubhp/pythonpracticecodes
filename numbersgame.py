import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0

is_running = True

print("Welcome to Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter the guessing number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("The guess is out of range")
            print(f"Select the number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Invalid Guess!")
            print("The answer is higher number")
        elif guess > answer:
            print("Invalid Guess")
            print("The answer is lower number")
        else:
            print("Congratulations! The guess is correct.")
            print("Thank You for playing the game.")
            print(f"number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
