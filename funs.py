#function is a block which containt some code but excute whenever we will call it

def sum():
    x=2
    y=3
    z=x+y
    print("sum is ",z)

def sub():
    x=10
    y=2
    z=x-y
    print("sub is ",z)

def multiply():
    x=10
    y=2
    z=x*y
    print("multiply is ",z)   

ch=int(input("1 for sum 2 for sub 3 for multply"))
if ch==1:
    sum()
elif ch==2:
    sub()
elif ch==3:
    multiply()
else:
    print("no choice")  



           
            


