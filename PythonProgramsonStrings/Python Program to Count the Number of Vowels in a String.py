s = input("Enter String: ")

count = 0
for x in s:
    if x.lower() in ["a","e","i","o","u"]:
        count = count + 1

print("Number of vowels are:")
print(count)
