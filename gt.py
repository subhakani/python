A=[]
N=int(input("n="))
if(1<=N<=1000):
   print("enter your",N,"integer")
   for i in range(1,N+1):
       a=int(input("c="))
       A.append(a)
   print(sorted(A))
   median=sorted(A)[len(A)//2]
   print(median)
else:
    print("invalid")
