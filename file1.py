f=open("me.md","w")
s=input("enter message here")
f.write(s)
f.close()

# f=open("me.md","r")
# print(f.read())
# f.close()


# d=[]
# ans=True
# f=open("datas.txt","a")
# while ans==True:
#     v=input()
#     if v=="quit":
#         ans=False
#     #d.append(v)    
#     f.write(v+"\n")
# f.close()

# f=open("datas.txt","r")
# print(f.readline())
# f.close()

import os
os.remove("me.md")
print("delted")
