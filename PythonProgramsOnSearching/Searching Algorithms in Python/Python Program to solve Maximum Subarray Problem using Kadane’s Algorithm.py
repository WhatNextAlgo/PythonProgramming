def find_max_subarray(alist,start,end):

    left_index = left_index_so_far = start
    max_right_index = start + 1
    max_val = max_seen_so_far = alist[start]

    for x in range(start + 1,end):
        if max_val > 0:
            max_val += alist[x]
        else:
            max_val = alist[x]
            left_index = x

        if max_val > max_seen_so_far:
            max_seen_so_far = max_val
            left_index_so_far = left_index
            max_right_index = x + 1

    return left_index_so_far,max_right_index,max_seen_so_far



alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
