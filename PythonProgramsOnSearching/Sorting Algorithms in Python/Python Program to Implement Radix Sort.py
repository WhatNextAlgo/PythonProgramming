def counting_sort(alist,largest,key):
    c = [0] * (largest + 1)

    for x in range(len(alist)):
        c[key(alist,x)] = c[key(alist,x)] + 1
    
    print(c)

    c[0] = c[0] -1 
    for x in range(1, largest + 1):
        c[x] = c[x] + c[x-1]
    
    result = [None] * len(alist)

    for x in range(len(alist)-1,-1,-1):
        result[c[key(alist,x)]] = alist[x]
        c[key(alist,x)] = c[key(alist,x)] -1

    return result


def radix_sort(alist, base=10):
    if alist == []:
        return
    def key_factory(digit,base):
        def key(alist,index):
            return ((alist[index]//base**digit) % base)
        return key

    exp = 0
    largest = max(alist)
    while base** exp <= largest:
        alist = counting_sort(alist,base-1,key_factory(exp,base))
        exp = exp + 1
    
    return alist

alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [int(x) for x in alist]
sorted_list = radix_sort(alist)
print('Sorted list: ', end='')
print(sorted_list)


