n=6
n=n+1
for i in range(1,n):
    for j in range(1,(2*(n-1))):
        print("",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()   
