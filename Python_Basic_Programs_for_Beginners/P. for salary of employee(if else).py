ch=input("Enter the sex of employee (m or f):")
sal=int(input("Enter the salary of the employee:"))

if (ch=='m'):
    if sal<10000:
        bonus=0.07*sal
    else:
        bonus=0.05*sal
        
else:
    if sal<10000:
        bonus=0.12*sal
    else:
        bonus=0.10*sal
        
amount=sal+bonus
print("Salary=",sal)
print("Bonus=",bonus)
print("*****************************")
print("Amount to be paid:",amount)
