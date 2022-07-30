from itertools import count


s = input("Enter String: ")

vowels = set("aeiou")

count = 0
for  letters in s:
    if letters in vowels:
        count += 1

print("Count of the vowels is:")
print(count)
