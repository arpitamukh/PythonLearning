# take three values from user
import keyword


x = int(input("Enter the value of X: "))
y = float(input("Enter the value of Y: "))
z = float(input("Enter the value of Z: "))
sum = x + y + z
b=(max(x,y,z))
# Display all values on screen
print("\n")

with open('lab005.txt', 'w') as file:
    print("SUM", sum, sep=' :-->', file=file, flush=True)
    print("max value", b, sep=' :-->', file=file, flush=True)
    print("type of x" ,type(x), "type of y", type(y),"type of z",type(z), sep=' :-->', file=file, flush=True)

    ##print("happy")
