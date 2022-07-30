s = input("Enter String: ")

count = 0
for x in s:
    if x.islower():
        count = count + 1

print("The number of lowercase characters is:")
print(count)