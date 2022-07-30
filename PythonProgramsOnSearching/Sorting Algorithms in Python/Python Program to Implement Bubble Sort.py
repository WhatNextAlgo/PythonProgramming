def bubble_sort(alist):
    for x in range(len(alist)-1,0,-1):
        no_swap = True
        for y in range(0,x):
            if alist[y] > alist[y + 1]:
                alist[y], alist[y + 1] = alist[y + 1], alist[y]
                no_swap = False
        if no_swap:
            return


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print('Sorted list: ', end='')
print(alist)

