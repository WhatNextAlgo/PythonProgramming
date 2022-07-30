def select(alist,start,end,i):
    if end - start <=1:
        return alist[start]
    
    pivot = partition(alist,start,end)
    k = pivot -start + 1

    if i < k:
        return select(alist,start,pivot-1,i)

    elif i > k:
        return select(alist,pivot + 1,end,i - k)

    return alist[pivot]

def partition(alist,start,end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j -1

        if i <= j:
            alist[i],alist[j] = alist[j],alist[i]
        else:
            alist[start],alist[j]= alist[j],alist[start]
            return j

alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
i = int(input('The ith smallest element will be found. Enter i: '))
 
ith_smallest_item = select(alist, 0, len(alist), i)
print('Result: {}.'.format(ith_smallest_item))