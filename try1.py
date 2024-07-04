# x=10
# y=2

# try:
#     z=x/y
#     print("ans is ",z)
# except Exception as e:
#     pass 

# z=x+y
# print("sum is",z)

x=20
y=2
try:
    if y<0 or y==1:
        raise Exception("1 and negative values are not allowed")

    else:
        z=x/y
        print("ans is ",z)
except Exception as e:
    print("error",e)        