def binary_search(alist,key):

    start = 0
    end = len(alist) -1
    while end - start >= 0: # start < end
        mid = (start + end)//2

        if alist[mid] < key:
            start = mid + 1
        elif alist[mid] > key:
            end = mid -1
        else:
            return mid
    return -1


alist = input('Enter the sorted list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))
 
index = binary_search(alist, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))

        
    
