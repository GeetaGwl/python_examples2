# '''
# a varible which store no of valus 
# 1 list=[] fully editable
# 2 tuple=() not editable
# 3 set={}   not breakable not index not dublicate shuffled but try to rrange in assending order
# 4 dict={,} with index
# '''

# a=[2,5,2,2,78,23.8,10]

# '''
# 0 2
# 1 5
# 2 2
# 3 2
# 4 78
# 5 23.8
# 6 10  #a.insert(10,3) # using insert i can put new value at particuler index without deleteing existed value
# # slice tool use to get some value from collection
# #print(a[:5]) # auto start from begening
# #print(a[1:]) # auto last  [ start : end : steps]
# '''
# a[0]=1
# b=[11,12,13,14,15,16,17,18,19,20] # left to right 0 to 9 , right to left -1 to -10
# #print(b[-1:-4:-2  ])
# # add new element in list
# # b.insert(3,100)
# # print(b)
# # b.append(200) # add value in last position
# # print(b)
# # c=[101,102,103]
# # #b.extend(c)
# # b.append(c)
# # print(b)
# # # remove value from list
# # b.remove(13)
# # print(b)
# # b.pop() # remove from last
# # print(b)
# # del b[6] # remove using index
# # print(b)
# # b[0]=110
# # print(b)
# # print(a)
# # print(a+b)
# # print(a*2)

# x=(100,200,300,400,500,200,200)
# print(x[0:3])
# print(x.index(300))
# print(b.index(18))

# print(b[::-1])
# print(a)
# print(sorted(a))
# print(len(b))
# d=b.copy()
# e=b
# b[0]=90
# print(d,b,e)
# a=(1,2,3)
# l=list(a)
# l.append(4)
# a=tuple(l)
# print(a)
# set is a collection of data but it has no index {} dublicate value not add its shuffled and try to arreange in assending order

# s={10,6,4,3,2,11,15,6,12,8}

# s.add(13)
# s.update([17,18,16])
# print(s)
# s.remove(15)
# s.pop() # its use to remove value from first position
# s.pop()
# print(s)

# dict is also collection of data and accept values in pair form first is index called key and second is value

d={1:"Delhi",2:"Mumbai",3:"Bhopal",4:"Banglor",5:"Gwalior"}

#print(d[6])
d2={"userid":"Admin","Password":12345,"age":27,"Address":"ghhjg"}
print(d2["userid"])
print(d2["Password"])
print(d2.get("age"))

l1=[1,2,3,4]
l2=["aa","bb","cc"]
d3=dict(zip(l1,l2))
print(d3,d2)
print(l1+l2)

























