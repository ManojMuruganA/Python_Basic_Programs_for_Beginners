string=input("Enter the string:")

vowels=0
consonants=0

for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels+=1
    else:
        consonants+=1

print("No. of vowels:",vowels)
print("No. of consonants:",consonants)
    
