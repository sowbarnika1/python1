n=int(input())
for i in range(1,n):
    if(i==1 or i==n):
        if(n%i==0):
            f=1
    else:
        if(n%i==0):
            f=0 
            break
if(f==1):
    print("prime")
else:
    print("not prime")
