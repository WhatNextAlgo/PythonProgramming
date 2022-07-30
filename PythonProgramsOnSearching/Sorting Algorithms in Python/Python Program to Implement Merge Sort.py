def merge(alist,start,mid,end):
    left = alist[start:mid]
    right = alist[mid:end]

    i = 0 # left index
    j = 0 # right index
    k = start # merge index

    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j =  j + 1

        k = k + 1

    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k  = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k  = k + 1

def merge_sort(alist,start,end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist,start, mid)
        merge_sort(alist,mid ,end)
        merge(alist,start,mid,end)





alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist)-1)
print('Sorted list: ', end='')
print(alist)
    

