#Star patten

n=int(input("enter the no of the rows"))
for i in range(1,n+1):
    for j in range(i):
        print(" * ",end="")
    print()