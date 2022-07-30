print("Enter a hyphen separated sequence of words:")

a = input().split("-")
a.sort()
print("-".join(a))
