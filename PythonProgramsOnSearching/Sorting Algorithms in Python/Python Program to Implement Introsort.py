
def introsort(alist):
    maxdepth = (len(alist).bit_length() - 1)*2
    introsort_helper(alist, 0, len(alist), maxdepth)

def introsort_helper(alist,start,end,maxdepth):
    if end- start <= 1:
        return
    elif maxdepth == 0:
        heap_sort(alist)
    else:
        p = partiton(alist,start,end)
        introsort_helper(alist,start,p+1,maxdepth -1)
        introsort_helper(alist,p+1,end,maxdepth -1)

def swap(alist,start,index):
    alist[start],alist[index] = alist[index],alist[start]

def partiton(alist,start,end):
    pivot = alist[start]
    i = start + 1
    j = end -1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j -1

        if i <= j:
            swap(alist,i,j)
        else:
            swap(alist,start,j)
            return j


def heap_sort(alist):
    build_max_heap(alist)
    for i in range(len(alist)-1,0,-1):
        swap(alist, 0, i)
        max_heapify(alist, index=0,size=i)

def build_max_heap(alist):
    def parent(index):
        return (index - 1)//2
    length = len(alist)
    start = parent(length -1)
    while start >= 0:
        max_heapify(alist,index = start,size=length)
        start = start -1


def max_heapify(alist,index,size):
    def left(index):
        return 2 * index + 1

    def right(index):
        return 2 * index + 2

    l = left(index)
    r = right(index)

    if l < size and alist[l] > alist[index]:
        largest = l
    else:
        largest = index

    if r < size and alist[r] > alist[largest]:
        largest = r

    if largest != index:
        swap(alist,largest,index)
        max_heapify(alist,largest,size)


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
introsort(alist)
print('Sorted list: ', end='')
print(alist)

        
