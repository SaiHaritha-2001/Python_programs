#swapping using temp
'''a=10
b=20
print("After Swapping")
temp=a
a=b
b=temp
print("a=",a,"b=",b)
'''
#swapping without using temp
a=int(input("enter the number"))
b=int(input("enter the value"))
print("After swapping")
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)