def selection_sort(alist):
    for x in range(len(alist)-1):
        smallest = x
        for j in range(x + 1, len(alist)):
            if alist[smallest] > alist[j]:
                smallest = j
        alist[x], alist[smallest] = alist[smallest], alist[x]


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('Sorted list: ', end='')
print(alist)