import sys
import math

x = int(input("Enter the value of X: "))
y = float(input("Enter the value of Y: "))
z = float(input("Enter the value of Z: "))
sum = x + y + z
mul = x * y * z
sum = sum - 10
sum = sum + 10
#variable should be store in variable
sum = sum + 10

print("sum of the three numbers", sum)
formatted_number = f"{y:.4f}"
print("formatted number : ", formatted_number)

print(sys.maxsize)

name = input("Enter the name: ")
print("hi", name)
