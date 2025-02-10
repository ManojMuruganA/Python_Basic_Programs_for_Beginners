def pascalTriangle(n):
    for i in range(0,n):
        c=1
        for j in range(1,n-i):
            print("  ",end=" ")
        for k in range(0,i+1):
            print("  ",c,end=" ")
            c=c*(i-k)//(k+1)
        print()

n=int(input("Enter the number of rows: "))

pascalTriangle(n)
