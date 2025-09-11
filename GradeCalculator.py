Maths=int(input("Enter Maths Marks:"))
Sci=int(input("enter Science Marks:"))
Eng=int(input("Enter English Marks:"))
Total=Maths+Sci+Eng
print("Total Marke :",Total)
Avg=Total/3
print("Average Marks:",Avg)
if(Avg>90 and Avg<100):
    print("Garede:O ")
elif(Avg>80 and Avg<90):
    print("Grade:A")
elif(Avg>60 and Avg<80):
    print("Grade:B")
else:
    print("Read Well.....")