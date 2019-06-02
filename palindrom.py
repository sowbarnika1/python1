n=int(input())
k=n;
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(k==rev):
    print("palindrom")
else:
    print("not palindrom")
