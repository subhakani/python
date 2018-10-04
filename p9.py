x=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(x,b,end=" ")
while(n-2):
    c=x+b
    x=b
    b=c
    print(c,end=" ")
    n=n-1
