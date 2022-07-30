s = input("Enter String: ")

upper_count = 0
lower_count = 0

for  x  in s:
    if x.islower():
        lower_count = lower_count  + 1

    else:
        upper_count = upper_count + 1


print("The number of lowercase characters is:")
print(lower_count)
print("The number of uppercase characters is:")
print(upper_count)    