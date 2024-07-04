import libs as l
#n=int(input("enter no"))
#l.table(n)
#l.areaofcircle(4)
#l.si(20000,3,5)
#l.values(1,2,3)
#l.sum()

import retfun as r 
ans=r.sum(10,2)
print("ans is",ans)

c=r.squre(2)
print("cube is",c)
print(r.sum(3,4))
a,b=r.swap(10,20)
print(a)
print(b)
r.ss()

ans=lambda x,y: x+y
print(ans(2,3))

intr=lambda p,r,t: (p*r*t)/100
print("intrest is",intr(1000,3,4))
