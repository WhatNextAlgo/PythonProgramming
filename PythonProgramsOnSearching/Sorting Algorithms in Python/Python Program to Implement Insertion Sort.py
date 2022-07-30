def insertion_sort(alist):
    for i in range(1,len(alist)):
        temp = alist[i]
        j = i -1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j+1] = temp

#start index  is 1 
#2 4 1 5 8 0
#2 4 1 5 8 0
#2 1 4 5 8 0
#1 2 4 5 8 0

alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)