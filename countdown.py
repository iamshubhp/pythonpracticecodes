
# Importing library time
import time

# variable my_time with the user input in integer
my_time = int(input("Enter the time in seconds: "))

# X is out counter which keeps track of the countdown numbers
for x in range(my_time, 0, -1):

    # Counts seconds in the digital clock
    seconds = x % 60

    # Counts minutes in the digital clock
    minutes = int(x / 60) % 60

    # Counts hour in the digital clock
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Times Up!")
