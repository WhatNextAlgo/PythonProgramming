
def bubble_sort(alist):
    for x in range(len(alist)):
        for y in range(0,len(alist)-x-1):
            if alist[y] > alist[y + 1]:
                alist[y], alist[y + 1] = alist[y + 1],alist[y]
            
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
bubble_sort(a)
print('Second largest number is:',a[n-2])
