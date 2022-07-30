def binary_insertion_sort(alist):
    for x in range(1,len(alist)):
        temp = alist[x]
        pos = binary_search(alist,temp,0,x) + 1

        for y in range(x,pos,-1):
            alist[y] = alist[y-1]

        alist[pos] = temp
 
def binary_search(alist, key, start, end):
    if end - start <=1:
        if key < alist[start]:
            return start -1
        else:
            return start

    mid = (start + end)//2
    if alist[mid]< key:
        return binary_search(alist,key,mid,end)
    elif alist[mid] > key:
        return binary_search(alist,key,start,mid)
    else:
        return mid
 
 
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
binary_insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)
