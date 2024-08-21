'''
Task #8
✅ Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
 isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

'''

S1 = float(input("Enter length of triangle of one side(S1) :"))
S2 = float(input("Enter length of triangle of one side(S2) :"))
S3 = float(input("Enter length of triangle of one side(S3) :"))

if (S1 == S2 == S3):
    print("The triangle is equilateral")
elif (S1 == S2 or S2 == S3 or S1 == S3):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")


'''
OUTPUT:


Enter length of triangle of one side(S1) :12
Enter length of triangle of one side(S2) :12
Enter length of triangle of one side(S3) :12
The triangle is equilateral


Enter length of triangle of one side(S1) :19
Enter length of triangle of one side(S2) :20
Enter length of triangle of one side(S3) :23
The triangle is scalene






'''