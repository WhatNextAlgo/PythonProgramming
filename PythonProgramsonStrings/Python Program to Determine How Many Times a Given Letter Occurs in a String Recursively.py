def check(s,ch):
    if len(s) == 0:
        return 0

    elif s[0] == ch:
        return 1 + check(s[1:],ch)
    else:
        return check(s[1:],ch)

s = input("Enter String: ")
ch= input("Enter character to check:")
print("Count is:")
print(check(s,ch))
