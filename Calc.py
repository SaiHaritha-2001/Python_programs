num_1=int(input("Enter the 1st number:"))
num_2=int(input("Enter the 2nd number:"))
operator=input("Enter the operator")
if operator=="+":
    print("The Addition is",num_1+num_2)
elif operator=="-":
    print("The Subtractioin is",num_1-num_2)
elif operator=="*":
    print("The multiplication is",num_1*num_2)
elif operator=="/":
    print("The division is",num_1/num_2)
else:
    print("please enter  a valid number.....!")

