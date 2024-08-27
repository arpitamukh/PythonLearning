# print first 10 even number in reverse order
for i in range(10,0,-1):
    if i % 2 != 0:
        continue
    print(i, end=" ")
