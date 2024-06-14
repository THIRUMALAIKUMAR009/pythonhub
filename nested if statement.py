m1=int(input("Enter mark-1 : "))
m2=int(input("Enter mark-2 : "))
m3=int(input("Enter mark-3 : "))
total=m1+m2+m3
average=total/3.0
if m1>=35 and m2>=35 and m3>=35:
    print("result :pass")
    if average>=90 and average<=100:
        print("grade :A")
    elif average>=80 and average<=89:
        print("grade :B")
    elif average>=70 and average<=79:
        print("grade :c")    
    else:
        print("grade :d")
else:
    print("result :fail")
    print("grade  :no grade")
