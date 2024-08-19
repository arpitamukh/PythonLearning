### Task #4
# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

import math

r = float(input("Enter the radius of the circle :\n"))
π = 3.14
area = π * (r ** 2)
print(f"AREA of the circle for radius value:{r} is:", f"{area:.3f}")

'''
OUTPUT:
Enter the radius of the circle :
2
AREA of the circle for radius value:2.0 is: 12.560
'''


