sum=[]
N=int(input("n="))
if(1<=N<=1000):
   print("enter your",N,"integer")
   for i in range(1,N+1):
       a=int(input("c="))
       sum.append(a)
   print(sorted(sum))
   median=sorted(sum)[len(sum)//2]
   print(median)
else:
    print("invalid")
