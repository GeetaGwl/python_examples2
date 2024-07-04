

# if(a>b):
#     c=a+b
#     print("ans is ",c)
#     print("hi")
# else:
#     print("hello") 

# print("end if")   

# a=int(input("enter a"))
# if(a>=0):
#     print("its positive")
# else:
#     print("its negative")  

# gst=0
# ai=int(input("enter annual income"))
# if ai>700000:
#     gst=(ai*18)/100
#     print("gst is ",gst)
# else:
#     print("you dont need to pay gst")
#     print("gst is ",gst)    

# a,b,c=12,16,30
# if a>b and a>c:
#     print("a is greater then b and c")
# elif b>a and b>c:
#     print("b is greater then a and c")   
# else:
#     print("c is greater then a and b")   

# per=65
# if(per>90):
#     print("A+")
# elif(per>80):
#     print("A")
# elif(per>70):
#     print("B+")
# elif(per>60):
#     print("B")
# elif(per>50):
#     print("C")
# else:
#     print("D")                    
# a,b,c=12,3,10
# if(a>b):
#     if(a>c):
#         print("a is greater")
#     else:
#         print("c is greater")    
# elif(b>c):
#     print("b is greate")
# else:
#     print("c is greater")    
# wt=int(input("enter score of written test"))
# if(wt>70):
#     print("cleared first rount")
#     gd=int(input("enter marks of gd"))
#     if(gd>85):
#         print("you cleraed gd")
#         pi=int(input("enter marks of pi"))
#         if(pi>95):
#             print("congrats you got this job")
#         else:
     
#             print("you ccoul't clear pi")    
#     else:
#         print("gd not clear")  
# else:
#     print("wt not clear")       

print("welcome in kbc")
amt=0
print("who is pm of india")
print("1 modi 2 rahul 3 xyz 4 abc")
ans=int(input("enter choice"))
if(ans==1):
    print("graet ans is correct")
    amt=1000
    print("what is capitl of india")
    print("1 mumbai 2 delhi 3 banloe 4 other")
    ans=int(input("enter ans"))
    if(ans==2):
        print("ans is right")
        amt+=2000
        print("who is cm of delhi")
        print("1  abc 2 aaa 3 bbb 4 kajriwal")
        ans=int(input("enter ans"))
        if(ans==4):
            print("congrats you won this game")
            amt+=3000
        else:
            print("ans is wrong ")    
    else:
        print("ans is wrong")
else:
    print("better luck for next time")  


print("your amount is ",amt)          















