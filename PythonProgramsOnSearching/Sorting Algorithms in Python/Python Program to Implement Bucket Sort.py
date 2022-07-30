
def insertion_sort(alist):
    for x in range(1,len(alist)):
        temp = alist[x]
        j = x -1 
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j = j -1
        alist[j + 1] = temp


def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length

    print("largest ",largest," length ",length," size ",size)

    buckets = [[] for _ in range(length)]

    for i in range(length):
        j = int(alist[i]/size)
        print(alist[i]/size)
        print("j",j)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length -1].append(alist[i])

    print(buckets)

    for x in range(length):
        insertion_sort(buckets[i])

    result = []
    for x in range(length):
        result = result + buckets[x]

    return result


alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [int(x) for x in alist]
sorted_list = bucket_sort(alist)
print('Sorted list: ', end='')
print(sorted_list)