def sum(x=3,y=2):
    
    z=x+y
    print("sum is",z)




def si(p,r,t):
    
    i=(p*r*t)/100
    print("simple int is",i)   


def areaofcircle(r):
    
    p=3.14
    ar=p*r*r
    print("area is",ar)
 
def table(x):
    
    for i in range(1,11):
        print(i*x)
#passing parameter

def values(*l):
    print(l)