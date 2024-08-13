'''
--------------------------------------------------------------------------------
Create a program , take 2 inputs from the user num1, num2 and give them
#max
#pow num1 to num2
#sub, mul, sum, div.
Format your out with f{""}
You need to share this via the GITHUB repo ##
-------------------------------------------------------------------------------------
'''

num1 = float(input("Enter the value of num1 : "))
num2 = float(input("Enter the value of num1 : "))
#list = [num1, num2]
# quotient, remainder = divmod(num1, num2)
# remainder =divmod(num1,num2)

# with open('Outputlab008.txt', 'w') as file:


print(f"Maximum number between {num1} and {num2}is= {max(num1, num2)}")
print(f"The {num1} to the power of {num2} is = {pow(num1, num2)}")
print(f"Sum of {num1} and {num2} is ={num1+num2}")
print(f"Sub is {num1}-{num2}={num1-num2}")
print(f"Multiplication is {num1}*{num2}={num1*num2}")
print(f"Division is {num1}/{num2}={num1/num2:.3f}")
