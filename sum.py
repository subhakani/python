n=int(input("enter a number:"))
if(n < 0):
   print("enter a positive number")
else:
   sum = 0
   while(n > 0):
       sum += n
       n -= 1
   print("The sum is",sum)
