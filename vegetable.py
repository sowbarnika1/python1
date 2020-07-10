class Vegetable:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
class Store:
    def __init__(self,storename,veglist):
        self.storename=storename
        self.veglist=veglist
        
    def getAlphaorder(self):
        d={}
        for i in self.veglist:
            if i.name()[0] in d:
                d[i.name()[0]].append(i.name())
            else:
                d[i.name()[0]]=[i.name()]
        return d
        
    def filterVeg(self):
        temp=[]
        for i in self.veglist:
            if(i.price>=mn and i.price<=mx):
                temp.append(i.name())
        return temp
n=int(input())
veglist=[]
for i in range(n):
    name=input()
    price=float(input())
    quantity=int(input())
    t=Vegetable(name.lower,price,quantity)
    veglist.append(t)
    

storename=input()
mn=float(input())
mx=float(input())

s=Store(storename,veglist)
res1=s.getAlphaorder()
for i in sorted(res1):
    print(i)
    t=res1[i]
    for j in t:
        print(j)
res2=s.filterVeg()
if (res2==[]):
    print("no result found")
else:
    print(str(mn)+"-"+str(mx))
    for i in sorted(res2):
        print(i)

