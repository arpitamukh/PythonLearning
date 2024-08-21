'''
Task #9
✅ FizzBuzz Test: Write a program that prints numbers from 1 to 100. # Loop For However, for multiples of 3,
print "Fizz" instead of the number,
and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."

'''

with open('outputlab020.txt', 'w') as file:
    for i in range(1, 100):

        if i % 3 == 0 and i % 5 == 0:
            # print("FizzBuzz")
            file.write(f"The number {i}, multiples of 3,5 replaced 'FizzBuzz'\n")
        elif i % 3 == 0:
            # print(f"the number {i} will be replaced by 'Fizz'")

            file.write(f"The number {i}, multiples of 3 replaced 'Fizz'\n")
        elif i % 5 == 0:
            # print(print(f"the number {i} will be replaced by 'Buzz'"))
            file.write(f"The number {i}, multiples of  5 replaced 'Buzz'\n")

        else:
            # print(f"the number is {i} ")
            file.write(f"the number is {i}\n ")
