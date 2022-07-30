a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)

count = 0
num=int(input("Enter the number to be counted:"))

for x in a:
    if x == num:
        count = count + 1

print("Number of times",num,"appears is",count)
    