# Dice Rolling Game in Python

import random



while True:

    user = input("Enter YES to roll the dice and NO to stop rolling: ").lower()

    if user == "yes":
        random_roll = random.randint(1, 6)
        print(f"Your dice number is {random_roll}")
        
    elif user == "no":
        print("Thanks for playing the dice roll game!")
        break
    
    else:
        print("Enter the valid response (YES) or (NO)")
        
     



