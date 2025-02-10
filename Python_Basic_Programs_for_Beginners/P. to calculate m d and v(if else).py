result=0

mdv=input("Choose one to calculate(m,d,v):")

if mdv=='m':
    d=float(input("Density:"))
    v=float(input("Volume:"))
    result=("Mass is:"+str(d*v))
elif mdv=='d':
    m=float(input("Mass:"))
    v=float(input("Volume:"))
    result=("Density is:"+str(m/v))
elif mdv=='v':
    m=float(input("Mass:"))
    d=float(input("Density:"))
    result=("Volume is:"+str(m/d))

print(result)
