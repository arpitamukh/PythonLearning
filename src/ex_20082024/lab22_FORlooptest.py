x = list(range(1, 10 + 1, 1))
print("Print x:", x)

y = list(range(1, 10 + 2, 2))
print("Print x,y:", x, y)


##To avoid printing a comma after the last number in Python
for i in range(10, 20, 1):
    if i == 19:
        print(i)
    else:
        print(i, end=",")

# for arpita in range(100, 150, 1):
#     print(arpita, end=" ")


for a in range(10, 0, -2):
        print("Hello World :",a)

for b in range(0, -10, -2):
            print(b,end=" ")

