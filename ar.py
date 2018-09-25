def kLargest(a, k):
    a.sort(reverse=True)
    for i in range(k):
        print (a[i],end=" ") 
a = [1, 23, 12, 9, 30, 2, 50]
k = 3
kLargest(a, k)
