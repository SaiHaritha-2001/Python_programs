a=int(input("Enter th num_1"))
b=int(input("Enter th num_2"))
c=int(input("Enter th num_3"))
#(-b+sqrt(b^2-4ac))/2a
d=(b*b)-4*a*c
Root1=(-b+d)/2*a
Root2=(-b-d)/2*a
print(f"Roots:"({Root1,Root2}),sep=",")