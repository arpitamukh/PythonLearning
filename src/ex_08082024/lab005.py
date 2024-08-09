# take three values from user
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
z = int(input("Enter the value of Z: "))
a = x+ y+ z
# Display all values on screen
print("\n")

with open('lab005.txt','w') as file:
    print("SUM",a, sep=' :-->',file=file,flush=True)
