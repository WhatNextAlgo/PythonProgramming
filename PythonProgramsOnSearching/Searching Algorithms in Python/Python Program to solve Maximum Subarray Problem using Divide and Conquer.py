def find_max_subarray(alist,start,end):
    print("start index : ",start,"end index : ",end)
    if start == end -1 :
        return start, end , alist[start]

    mid = (start + end)//2
    print("mid = ",mid)
    left_start,left_end,left_max = find_max_subarray(alist,start,mid)
    right_start,right_end,right_max = find_max_subarray(alist,mid,end)
    cross_start,cross_end,cross_max = find_max_crossing_subarray(alist,start,mid,end)
    if left_max > right_max and left_max > cross_max:
        return left_start,left_end,left_max
    elif right_max >left_max and right_max > cross_max:
        return right_start,right_end,right_max 
    else:
        return cross_start,cross_end,cross_max

def find_max_crossing_subarray(alist,start,mid,end):

    sum_left = float('-inf')
    sum_temp =0
    cross_left = mid
    print("start-mid",alist[start:mid])
    print("mid-end",alist[mid:end])

    for i in range(mid-1,start-1,-1):
        sum_temp =sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_left = i

    sum_right = float('-inf')
    sum_temp = 0
    cross_right = mid + 1
    for i in range(mid,end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right  = sum_temp
            cross_right  =  i + 1

    return cross_left,cross_right , sum_left + sum_right
                

alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))