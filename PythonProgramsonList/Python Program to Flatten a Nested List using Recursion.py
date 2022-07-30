def flatten(lst):
    if lst == []:
        return lst

    if isinstance(lst[0],list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])



s =[[1,2],[3,4]]
print("Flattened list is: ",flatten(s))