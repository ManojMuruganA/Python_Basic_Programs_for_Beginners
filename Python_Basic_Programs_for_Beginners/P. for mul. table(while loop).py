num=int(input("Enter the number:"))

print("The multiplication table is",num)

count=1
while count<=10:
    print(f"{num}X{count}={num*count}")
    count+=1
