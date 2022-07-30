def gnome_sort(alist):
    def swap(i,j):
        alist[i],alist[j] = alist[j],alist[i]
    for pos in range(1,len(alist)):
        while pos!=0 and alist[pos] < alist[pos-1]:
            swap(pos,pos-1)
            pos = pos -1



alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
gnome_sort(alist)
print('Sorted list: ', end='')
print(alist)