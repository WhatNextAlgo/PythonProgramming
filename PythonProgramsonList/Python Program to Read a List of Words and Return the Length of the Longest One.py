a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)

max_len = len(a[0])
temp = a[0]

for  x in a[1:]:
    if max_len < len(x):
        max_len = len(x)
        temp = x


print("The word with the longest length is:",temp, "len: ",max_len)
