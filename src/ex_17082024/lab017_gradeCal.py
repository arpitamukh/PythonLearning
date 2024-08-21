score = int(input("enter the score:"))
grade = ''

# Determine the grade based on the score
#if score >= 90 and score <= 100:
if 90 <= score <= 100:  # simplified chaining format
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

# Output the grade
print("Your grade is:", grade)
