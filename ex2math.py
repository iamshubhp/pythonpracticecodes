# Calculate the Area of the circle

import math

# formula to find area of the circle is: A = pi*r²

r = float(input("Enter the Radius of the circle: "))

area = math.pi * r**2

print(f"The area of the circle is {round(area, 2)} cm²")
 