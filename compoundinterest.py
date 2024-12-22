# Python compound interest calculator.

# --------------------------------------------------------------------------------------------------------
# this example is basic compund interest calculator.

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle amount cannot be less than or equal to 0")

# while rate <= 0:
#     rate = float(input("Enter the Interest Rate: "))
#     if rate <= 0:
#         print("Interest Rate cannot be less than or equal to 0")

# while time <= 0:
#     time = int(input("Enter the time period in year/s: "))
#     if time <= 0:
#         print("time period cannot be less than or equal to 0")

# total = principle * pow((1 + rate / 100), time)
# print(f"the balance after {time} year/s is : ${total: .2f}")

# --------------------------------------------------------------------------------------------------------

# in this method we will use boolean values such as True. as True is an boolean value the loop will run
# forever until we break it so we will also add break point with the help of else statement.

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount cannot be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the Interest Rate: "))
    if rate < 0:
        print("Interest Rate cannot be less than 0")
    else:
        break

while time <= 0:
    time = int(input("Enter the time period in year/s: "))
    if time < 0:
        print("time period cannot be less than 0")

    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"the balance after {time} year/s is : ${total: .2f}")
