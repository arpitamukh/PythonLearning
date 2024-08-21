'''
Task #7
✅ Leap Year Checker:
Create a program that determines whether a given year is a leap year. A leap year is divisible by 4,
but not by 100 unless it is also divisible by 400. Use an if-else statement to make this determination.
'''


year = int(input("Enter the year:"))

if year % 4 == 0 and year % 100 != 0:

    print(f"the year:{year} is leap year")

elif year % 400 == 0:

    print(f"the year:{year} is century leap year")

elif year % 100 == 0:

    print(f"the year:{year} is century ,not leap year")
else:
    print(f"the year:{year} is not leap year")


'''
OUTPUT:
Enter the year:222222
the year:222222 is not leap year


Enter the year:1900
the year:1900 is century ,not leap year

Enter the year:2000000
the year:2000000 is century leap year

'''