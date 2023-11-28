salary=int(input())
age=int(input())
if(salary>=20000 or age<=25):
    loan=int(input("loan:"))
    if(loan>50000):
        print("maximum loan amount is 50000")
    else:
         print("you are eligable for loan")

else:
    print("you are not eligable for loan")
