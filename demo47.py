def  palindrome(s):
    return s==s[::-1]
s="malayalam"
ans= palindrome(s)
if ans:
    print("yes")
else:
    print("no")
    
    
