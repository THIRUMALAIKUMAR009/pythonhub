def checkleap(year):
    if(year%400==0):
        if(year%100!=0):
        if(year%4==0):
        print ("the given year is a leap year")
    else:
        print("the given year is not a leap year")
        year=int(input("enter the number"))
checkleap(year)
