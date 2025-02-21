# Counter using Python functions and default arguments

import time


def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")


count(10)  # call any value you want to run the timer for


#  another example code for keyword arguments


def call(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


caller = call("1", "234", "567", "890")
print(caller)
