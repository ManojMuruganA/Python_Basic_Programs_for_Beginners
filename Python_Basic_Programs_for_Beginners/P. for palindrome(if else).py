def palindrome(s):
    return s==s[::-1]

s=input("Enter the string:")
ans=palindrome(s)

if ans:
    print("String is palindrome")
else:
    print("String is not palindrome")
