n=int(input())
a=[]
c1=[]
c2=[]
b=[]
mi=0
count=0
ans=0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(bin(a[i]).replace("0b",""))
    m=b[i]
    if(len(m)>mi):
        mi=len(m)
#print mi
for i in range(n):
    c1.append((b[i]).count("1"))
    c2.append((b[i]).count("0"))
    if(c1[i]+c2[i]!=mi):
        d=mi-(c1[i]+c2[i])
        c2[i]=c2[i]+d
    print c1[i],c2[i]
    if(c1[i]==c2[i]):
        ans=ans+1
for i in range(0,n):
    sum1=c1[i];
    sum2=c2[i];
    for j in range(i+1,n):
        sum1=sum1+c1[j]
        sum2=sum2+c2[j]
        if(sum1==sum2):
            ans=ans+1
for i in range(0,n):
    for j in range(i+2,n-1):
        if((c1[i]+c1[j]==c2[i]+c2[j])):
            ans=ans+1
print ans
t=bin(ans).replace("0b","")
print (t.zfill(mi))
