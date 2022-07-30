def comb_sort(alist):
    def swap(i,j):
        alist[i],alist[j]= alist[j], alist[i]

    gap = len(alist)
    shrink = 1.3
    no_swap = False

    while not no_swap:
        gap = int(gap/shrink)

        if gap < 1:
            gap = 1
            no_swap = True
        else:
            no_swap = False
        
        i = 0

        while i + gap < len(alist):
            if alist[i] > alist[i + gap]:
                swap(i,i + gap)
                no_swap = False
            i = i + 1


alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
comb_sort(alist)
print('Sorted list: ', end='')
print(alist)