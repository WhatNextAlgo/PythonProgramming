def sum_arr(lst):
    if lst == []:
        return 0

    return lst[0] + sum_arr(lst[1:])

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)




print("The list is:")
print(a)
print("Sum of items in list:")
b=sum_arr(a)
print(b)