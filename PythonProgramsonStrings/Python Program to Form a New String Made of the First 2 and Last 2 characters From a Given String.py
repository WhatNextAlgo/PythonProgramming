s1 = input("Enter first string: ")


new_string = s1[:2] + s1[-2:]
print(new_string)

count=0
for i in s1:
      count=count+1
new=s1[0:2]+s1[count-2:count]
print("Newly formed string is:")
print(new)