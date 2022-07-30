s = input("Enter string: ")

def ispalindrome(s):
    print(s)

    if len(s) < 1:
        return True

    if s[0] == s[-1]:
        return ispalindrome(s[1:-1])
    else:
        return False

if(ispalindrome(s)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")