class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def calResult(self):
        avg=0
        if(self.sub1>=40 and self.sub2>=40 and self.sub3>=40):
            avg=(self.sub1+self.sub2+self.sub3)/3
        return avg
    
class School:
    def __init__(self,schooln,d):
        self.schooln=schooln
        self.d=d
        
    def getStudentResult(self):
        for i in self.d:
            if (i.calResult()>60):
                self.d[i]="pass"
        return self.d
        
    def highestMark(self):
            m=0
            obj=None
            for i in self.d:
                if (i.calResult()>m and self.d[i]=="pass"):
                    m=i.calResult()
                    obj=i
            return obj

t=int(input())
d={}
for i in range(t):
    name=input()
    sub1=int(input())
    sub2=int(input())
    sub3=int(input())
    var=Student(name,sub1,sub2,sub3)
    d[var]="fail"
    
schooln=input()

s=School(schooln,d)
res1=s.getStudentResult()
res2=s.highestMark()

for i in res1:
    if (res1[i]=="pass"):
        print(i.name)
        
if(res2==None):
    print("no Student found")
else:
    print(res2.name)
    print(res2.calResult())
