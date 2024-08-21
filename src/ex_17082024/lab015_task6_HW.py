# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

x = float(input("enter the value for x:"))
y = float(input("enter the value for y:"))
z = float(input("enter the value for z:"))

# x = input("enter the value for x:")
# y = input("enter the value for y:")
if x < y and x < z:
    print(f"value of x-->{x} is less than value of y-->{y} and value of z-->{z}")
elif x > y and x > z:
    print(f"value of x-->{x} is greater than value of y-->{y}")

else:
    print(f"value of x-->{x} is equal to value of y-->{y}")

'''
OUTPUT :
========================================================
Scenario:1 (x<y)
enter the value for x:3.3
enter the value for y:4.4
value of x-->3.3 is less than value of y-->4.4

Scenario:2 (x>y)
enter the value for x:4
enter the value for y:3
value of x-->4 is greater than value of y-->3

Scenario:3 (x==y)
enter the value for x:44
enter the value for y:44.00
value of x-->44.0 is equal to value of y-->44.0
'''
