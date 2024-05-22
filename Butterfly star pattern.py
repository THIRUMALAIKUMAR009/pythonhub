n=6
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    spaces=2*(n-i)
    for j in range(0,spaces):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    spaces=2*(n-i)
    for j in range(0,spaces):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()    
