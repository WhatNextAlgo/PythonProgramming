
a = [[1,2],[3,4,[5]]]

def sum1(lst):
    total = 0

    for x in lst:
        if isinstance(x,list):
            total = total + sum1(x)
        else:
            total = total + x

    return total

print( "Sum is:",sum1(a))