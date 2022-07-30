def get_length(lst):
    if lst == []:
        return 0

    return 1 + get_length(lst[1:])

a=[1,2,3,4,5]
#a = []
print("Length of the string is: ")
print(get_length(a))