import random

# print(help(random))

# number = random.randint(1, 6)

low = 20

high = 100

options = ("rock", "paper", "scissors")

cards = ["2", "3", "4", "5", "6","7", "8", "9", "10", "J", "Q", "K","A"]

# number = random.randint(low, high) print any random integer between high and low
# number = random.random() # this will print a floating point number between 1 and 0.

# option = random.choice(options) # great method for games if we need to choose an element

random.shuffle(cards)
print(cards)