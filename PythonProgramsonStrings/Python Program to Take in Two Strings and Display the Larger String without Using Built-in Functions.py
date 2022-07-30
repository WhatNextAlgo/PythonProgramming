s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1= 0
count2 = 0
for x in s1:
    count1 = count1 + 1

for x in s2:
    count2 = count2 + 1


if(count1<count2):
      print("Larger string is:")
      print(s2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(s1)