num=int(input("Enter the number limit:"))
i=1
s=0

while(i<=num):
    s=s+i
    i=i+1
avg=s/num

print("The sum of first",num,"numbers is:",s)
print("The average of first",num,"numbers is:",avg)
