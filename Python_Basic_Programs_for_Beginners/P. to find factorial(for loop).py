num=int(input("Enter the number:"))

if(num==0):
    fac=1
else:
    fac=1
    for i in range(1,num+1):
        fac=fac*i

print("The factorial of",num,"is",fac)
