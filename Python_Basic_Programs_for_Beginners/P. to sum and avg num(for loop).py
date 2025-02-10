num=int(input("Enter a value:"))

avg=0
sum=0

for i in range(1,num+1):
    sum=sum+i
    
avg=sum/i
print("Sum of",num,"numbers is",sum)
print("Avg. 0f",num,"numbers is",avg)
