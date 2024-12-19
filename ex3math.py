# find the hypotenuse of a right triangle

import math

# formula to find hypotenuse of a right triangle: C = sqrt(a**2 + b**2)

a = float(input("Enter the value of side a: "))

b = float(input("Enter the value of side b: "))


c = math.sqrt(pow(a, 2) + pow(b, 2))

# c = math.sqrt(a**2 + b**2) we can also use this formula the formula above is same as this.

print(f"the hypnotenuse of the right angle triangle is {c}")
