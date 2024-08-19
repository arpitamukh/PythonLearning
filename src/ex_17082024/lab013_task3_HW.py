'''
#Task #3
--------------------------------------------------------------------------------
- Explain the difference between the = operator and the == operator in Python.
- What does the ** operator do in Python, and how is it used?
- What does the ^ operator do in Python, and in what context is it commonly used?
-------------------------------------------------------------------------------------



Solution or point 1:Explain the difference between the = operator and the == operator in Python.
*************************************************************************************************
In Python, the = and == operators serve different purposes:
1.
'=' Operator is (Assignment Operator).
The = operator is used to assign a value to a variable.
Example as below:
----------------------------------------------------------------
'''

x = 50
print(f"In Python '=' operator is for assignment,the value {x} is assigned to the variable x.")

# OUTPUT:In Python '=' operator is for assignment,the value 50 is assigned to the variable x.


'''
========================================================================
2.
== Operator is (Equality Operator)
The == operator is used to compare two values to check if they are equal.
It returns True if the values on both sides are equal, and False otherwise.
Example as below
===========================================================================
'''

a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
if (a == b):
    print(f"value of a :{a} is equal to value of b:{b}")
else:
    print(f"value of a :{a} is not equal to value of b:{b}")

'''
# OUTPUT :
# Scenario 1:-->where a and b are  equal:
enter the value of a:99
enter the value of b:99
value of a :99 is equal to value of b:99

# Scenario 2:-->where a and b are not equal:
# enter the value of a:3
# enter the value of b:4
# value of a :3 is not equal to value of b:4
'''

'''
-------------------------------------------------------------------------------------
Solution or point 2:What does the ** operator do in Python, and how is it used?
*************************************************************************************************
The ** operator in Python is used for exponentiation, raising a number to the power of another number.
Example is as below:
'''
a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
result = a ** b
print(
    f"In Python '**' operator is for exponentiation,The output of {a} raised to the power of {b} using the ** operator is {result}")

'''
OUTPUT:
enter the value of a:2
enter the value of b:4
In Python '**' operator is for exponentiation,The output of 2 raised to the power of 4 using the ** operator is 16
'''




'''
-------------------------------------------------------------------------------------
Solution or point 3:What does the ^ operator do in Python, and in what context is it commonly used?
*************************************************************************************************
The ^ operator in Python is primarily used for bitwise XOR operations
Example is as below:
'''

# a = 5  # binary: 0101
# b = 3  # binary: 0011
# result = a ^ b  # result: 0110 (which is 6 in decimal)
# print(result)

decimal_number_one = int(input("enter the value of decimal number1:"))
decimal_number_two = int(input("enter the value of decimal number2:"))
result = (decimal_number_one ^ decimal_number_two)
binary_representation_one = bin(decimal_number_one)
binary_representation_two = bin(decimal_number_two)
binary_representation_three = bin(result)
print(f"binary representation of decimal number1 is :{binary_representation_one}")
print(f"binary representation of decimal number2 is :{binary_representation_two}")
print(f"binary representation of final result after operation ({decimal_number_one}^{decimal_number_two}) is :{binary_representation_three}")

print(f"Decimal value of  of final result after operation ({decimal_number_one}^{decimal_number_two}) is: {(int(binary_representation_three,2))}")


# OUTPUT:
# enter the value of decimal number1:3
# enter the value of decimal number2:5
# binary representation of decimal number1 is :0b11
# binary representation of decimal number2 is :0b101
# binary representation of final result after operation (3^5) is :0b110
# Decimal value of  of final result after operation (3^5) is: 6