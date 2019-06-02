from array import *
arr=array('i',[])
n=int(input())
k=int(input())
for i in range(n):
    a=int(input())
    arr.append(a)
i=1
sum=0
for i in range(k):
    sum=sum+arr[i]
print("sum is",sum)

    
