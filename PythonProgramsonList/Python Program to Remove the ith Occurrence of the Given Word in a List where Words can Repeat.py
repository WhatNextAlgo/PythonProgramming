a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
print(a)
count = 0
b=input("Enter word to remove: ")
n=int(input("Enter the occurrence to remove: "))
c = []
for x in a:
    if x == b:
        count += 1
        if count != n:
            c.append(x)
    else:
        c.append(x)


if(count==0):
    print("Item not found ")
else: 
    print("The number of repetitions is: ",count)
    print("Updated list is: ",c)
    print("The distinct elements are: ",set(a))