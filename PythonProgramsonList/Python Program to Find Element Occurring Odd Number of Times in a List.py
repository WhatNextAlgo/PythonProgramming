def find_odd_occurring(lst):
    """Return the element that occurs odd number of times in alist.
 
    alist is a list in which all elements except one element occurs an even
    number of times.
    Since the XOR operation is commutative and associative and it satisfies p XOR p = 0 and p XOR 0 = p,
    the element that occurs an odd number of times is the result.
    """
    ans = 0
    for x in lst:
        ans ^= x

    return ans

alist = input('Enter the list: ').split()
alist = [int(i) for i in alist]
ans = find_odd_occurring(alist)
print('The element that occurs odd number of times:', ans)