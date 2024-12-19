# math Ex1 circumferenceof the circle C= 2pir

import math

r = float(input("Enter the radius of the circle: ")) 

c = 2 * math.pi * r

# prints the result of the circumference rounding up to 3 decimal poitns
print(f"The Circumference of the circle is {round(c, 3)} cm")
