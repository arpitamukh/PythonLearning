#The continue statement is used to skip the rest of the code inside
# the loop for the current iteration and move on to the next iteration.
#When continue is encountered, the current iteration of the loop is terminated early, and the loop proceeds to the next iteration.

#continue skips only the current iteration and proceeds with the next iteration of the loop.


for a in range(1, 10):
    if a % 2 == 0:
        continue
    else:
        print(a, end=" ")
print("\n")



# for i in range(1, 10):
#     if i % 2 == 0:
#         break
#     else:
#         print(i)
