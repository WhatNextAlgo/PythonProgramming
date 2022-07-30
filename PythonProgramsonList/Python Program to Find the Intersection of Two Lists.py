lst1 = [23,34,65]
lst2 = [33,23,65,86]

a = list(set(lst1) & set(lst2))
print('The Union of two lists is:',a)