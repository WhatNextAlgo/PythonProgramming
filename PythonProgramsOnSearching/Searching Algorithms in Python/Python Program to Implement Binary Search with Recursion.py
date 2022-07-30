def binary_search(alist, start, end, key):
    if end - start <= 0:
        return -1

    mid = (start + end)//2
    if alist[mid] > key:
        return binary_search(alist,start, mid-1,key)
    elif alist[mid] < key:
        return binary_search(alist,mid + 1, end,key)
    else:
        return mid


alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
